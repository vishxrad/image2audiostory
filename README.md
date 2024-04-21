# Image to Audio Story

This Streamlit app converts an uploaded image into an audio story. It utilizes machine learning models for image captioning and text generation, along with the Hugging Face API for text-to-speech conversion.

## How it Works

1. **Image Upload**: Users can upload an image of their choice.
2. **Image Captioning**: The app generates a descriptive caption for the uploaded image.
3. **Story Generation**: Based on the generated caption, a short story (within 100 words) is created.
4. **Text-to-Speech Conversion**: The story is then converted into an audio file using the Hugging Face API.
5. **Output Display**: The generated scenario, story, and audio file are displayed to the user.

## Setup

To run the app locally:

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up environment variables with your Hugging Face API token.
4. Run the main script `app.py`.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Transformers](https://huggingface.co/transformers/)
- [Requests](https://docs.python-requests.org/en/master/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [pytorch](https://pytorch.org)

## Usage

1. Upload an image using the file uploader.
2. Wait for the image caption and story to be generated.
3. Listen to the audio story.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the models and API used in this app.
- [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) for image captioning.
- [gpt-2-community](https://huggingface.co/gpt-2-community) for text generation. (Note: We are using GPT-2 from the gpt-2-community as it's lighter and more suitable for streaming via Streamlit.)
- [espnet/kan-bayashi_ljspeech_vits](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits) for text-to-speech conversion.

## Run Online

You can run this project online [here](https://imagetostory-visharad.streamlit.app).
