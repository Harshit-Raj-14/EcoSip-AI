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

cups_prompt='''Tell how many cups are there in the image. Only return the number of cups in image nothing else.'''

points_system_prompt=''' '''

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

def main():
    st.title("Eco Impact Tracker")
    st.write("Eco Sustainability Coins Calculator App: GreenRewards")

    # Use Streamlit's built-in camera input
    img_data = st.camera_input("Take a photo")

    if img_data:
        # Save and open the image using PIL
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshot_{timestamp}.jpg"
        with open(screenshot_path, "wb") as f:
            f.write(img_data.getbuffer())
        # st.success(f"Screenshot saved as {screenshot_path}")

        # Open the saved image using PIL
        image = Image.open(screenshot_path)

        # Display the image in the app
        # st.image(image, caption="Your Screenshot", use_column_width=True)

        # Call the Gemini API to analyze the image
        st.write("Scanning Image...")
        analysis_result = no_of_cups(image)

        if analysis_result:
            # Extract the predicted age from the response (if possible)
            try:
                predicted_cups = int("".join(filter(str.isdigit, analysis_result)))
                st.write(f"Estimated Cups: {predicted_cups}")
            except ValueError:
                st.error("Unable to extract cups from Gemini API response.")
        else:
            st.error("Failed to analyze the image.")

if __name__ == "__main__":
    main()