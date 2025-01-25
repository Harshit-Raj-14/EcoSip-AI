import streamlit as st
from PIL import Image
import os
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Load the API key from the .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the API key exists
if not GEMINI_API_KEY:
    raise ValueError("API key not found! Please add GEMINI_API_KEY to your .env file.")

# Authenticate with the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Prompts
cups_prompt = '''Tell how many cups are there in the image. Only return the number of cups in image nothing else.'''
thank_you_prompt = '''Generate a thank-you note for using biodegradable cups, explaining how it helps the environment, how much carbon footprint they saved, and a positive motivation to continue these practices. Use a friendly and encouraging tone.'''

def no_of_cups(image):
    try:
        # Load the generative model
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        
        # Generate content using the image and prompt
        response = model.generate_content([cups_prompt, image], stream=True)
        
        # Collect the streamed response
        streamed_text = ""
        for message in response:
            streamed_text += message.text  # Accumulate the streamed response
        
        # Return the final accumulated response text
        return streamed_text
    except Exception as e:
        st.error(f"Error using Gemini API: {e}")
        return None

def generate_thank_you_message(points, carbon_saved):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        response = model.generate_content([thank_you_prompt.format(points=points, carbon_saved=carbon_saved)], stream=True)
        
        # Collect the streamed response
        streamed_text = ""
        for message in response:
            streamed_text += message.text  # Accumulate the streamed response
        
        return streamed_text
    except Exception as e:
        st.error(f"Error using Gemini API: {e}")
        return None

def calculate_carbon_footprint(cups):
    # Assume each biodegradable cup saves 0.03 kg of carbon compared to a plastic cup
    carbon_saved_per_cup = 0.03  # in kg
    total_carbon_saved = cups * carbon_saved_per_cup
    return total_carbon_saved

def main():
    st.title("Eco Impact Tracker")
    st.write("Eco Sustainability Coins Calculator App: GreenRewards")

    # Provide a choice for the user
    choice = st.radio("Choose how to provide the photo:", ("Upload a Photo", "Take a Photo"))

    img_data = None

    if choice == "Upload a Photo":
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            img_data = uploaded_file
    elif choice == "Take a Photo":
        img_data = st.camera_input("Take a photo")

    if img_data:
        # Display the image preview
        st.image(img_data, caption="Uploaded Image Preview", use_container_width=True)

        # Process the image directly from the input
        image = Image.open(img_data)

        # Call the Gemini API to analyze the image
        st.write("Scanning Image...")
        analysis_result = no_of_cups(image)

        if analysis_result:
            # Extract the predicted number of cups
            try:
                predicted_cups = int("".join(filter(str.isdigit, analysis_result)))
                st.write(f"Estimated Cups: {predicted_cups}")

                # Calculate points and carbon footprint
                points = predicted_cups * 10  # Assign 10 points per cup
                carbon_saved = calculate_carbon_footprint(predicted_cups)
                
                st.write(f"🌟 Points Earned: {points}")
                st.write(f"🌍 Carbon Footprint Saved: {carbon_saved:.2f} kg")

                # Generate a thank-you message
                thank_you_message = generate_thank_you_message(points, carbon_saved)
                if thank_you_message:
                    # st.write("💚 Thank You Message:")
                    st.markdown("## 💚 Thank You Message:", unsafe_allow_html=True)
                    # st.write(thank_you_message)
                    st.markdown(thank_you_message, unsafe_allow_html=True)
                else:
                    st.error("Failed to generate thank-you message.")
            except ValueError:
                st.error("Unable to extract cups from Gemini API response.")
        else:
            st.error("Failed to analyze the image.")

if __name__ == "__main__":
    main()
