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

# Prompts for Gemini API
identify_prompt = "Analyze the image and identify what the object is. Describe it briefly."
eco_prompt = '''
Based on the identified object, provide:
1. Whether it is biodegradable or non-biodegradable.
2. Suggestions for how it can be recycled or disposed of responsibly.
'''

def analyze_image(image_path):
    try:
        # Load the generative model
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        
        # Load and convert image to bytes
        with open(image_path, "rb") as img_file:
            image_bytes = img_file.read()

        # Analyze the image and identify the object
        response = model.generate_content([identify_prompt, eco_prompt, image_bytes], stream=True)

        # Collect the streamed response
        streamed_text = ""
        for message in response:
            streamed_text += message.text

        return streamed_text
    except Exception as e:
        st.error(f"Error using Gemini API: {e}")
        return None

def chatbot_mode(chat_prompt):
    try:
        # Load the generative model
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        
        # Send user input to the chatbot model
        response = model.generate_content([chat_prompt], stream=True)
        
        # Collect the streamed response
        streamed_text = ""
        for message in response:
            streamed_text += message.text

        return streamed_text
    except Exception as e:
        st.error(f"Error in chatbot mode: {e}")
        return "Sorry, I couldn't process that."

def main():
    st.title("Smart Recycling Assistant")
    st.write("AI Recycle Bot App")

    # Use Streamlit's built-in camera input
    img_data = st.camera_input("Take a photo")

    if img_data:
        # Save and open the image using PIL
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = f"screenshot_{timestamp}.jpg"
        with open(image_path, "wb") as f:
            f.write(img_data.getbuffer())

        # Display the image in the app
        st.image(Image.open(image_path), caption="Uploaded Image", use_column_width=True)

        # Call Gemini API to analyze the image
        st.write("Analyzing Image...")
        analysis_result = analyze_image(image_path)

        if analysis_result:
            st.write("** Analysis:**")
            st.write(analysis_result)

            # Enable chatbot mode for further conversation
            st.write("Chat with Eco Bot about the image:")
            user_input = st.text_input("Ask Eco Bot something about the object or sustainability:")

            if user_input:
                chatbot_response = chatbot_mode(user_input)
                st.write(f"Eco  Bot: {chatbot_response}")
        else:
            st.error("Failed to analyze the image.")

if __name__ == "__main__":
    main()
