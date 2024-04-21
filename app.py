# Description: This is a Streamlit app that takes an image as input, generates a caption for the image, and then generates a story based on the caption. The story is then converted to an audio file using the Hugging Face API.

from dotenv import load_dotenv, find_dotenv
from transformers import pipeline
import requests
import os
import streamlit as st
import datetime

# Load environment variables (assuming you have API keys stored)
load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# Function for image captioning
def img2text(url):
    try:
        image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
        output = image_to_text(url)
        text = output[0]["generated_text"] if output and isinstance(output, list) and output[0] and "generated_text" in output[0] else None
        print("Image caption generated")
        return text
    except Exception as e:
        print("Error in image captioning:", e)
        return None


# Function for generating a story
def generate_story(scenario):
    # Format the scenario into the template
    template = f"You are a storyteller. Make sure the story has a proper ending. Don't ask any follow up questions and write a short story within 100 words based on the following sentence: {scenario}"

    # Initialize the text-generation pipeline with the LLAMA 3 model
    story_llm = pipeline("text-generation", model="meta-llama/Meta-Llama-3-8B", max_length=200)

    # Generate the story based on the template
    story = story_llm(template)

    # Extract the generated text 
    generated_text = story[0]['generated_text']
    prompt_length = len(template)

    story_without_prompt = generated_text[prompt_length:]
    print("Story generated")

    return story_without_prompt


def text2speech(message, folder_name="items"):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payload = {
        "inputs": message
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    # Generate a unique file name for each audio
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    audio_file = f"audio_{now}.flac"
    print("Audio generated")

    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Save the audio file in the specified folder
    audio_file_path = os.path.join(folder_name, audio_file)
    with open(audio_file_path, 'wb') as file:
        file.write(response.content)
    return audio_file_path


# Save the uploaded file to the items folder
def save_file_to_items_folder(file, folder_name="items"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_path = os.path.join(folder_name, file)
    return file_path


# Main function
def main():

    # Set the page title and icon
    st.set_page_config(page_title="Image to Audio Story", page_icon="🤖")
    st.header("Turn image into an audio story")
    uploaded_file = st.file_uploader("Choose an image: ", type="jpg")

    # Check if the file is uploaded
    if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            file_path = save_file_to_items_folder(uploaded_file.name)
            with open(file_path, "wb") as file:
                file.write(bytes_data)
            st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
            scenario = img2text(file_path)
            if scenario:
                story = generate_story(scenario)
                if story:
                    audio_file = text2speech(story)
                    if audio_file:
                        audio_file_path = audio_file
                        with st.expander("Scenario"):
                            st.write(scenario)
                        with st.expander("Story"):
                            st.write(story)
                        st.audio(audio_file_path)


# Run the main function
if __name__ == "__main__":
    main()
