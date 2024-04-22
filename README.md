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
- [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) for text generation.
- [espnet/kan-bayashi_ljspeech_vits](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits) for text-to-speech conversion.
## Run Online

- You can run this project online [here](https://imagetostory-visharad.streamlit.app).
- Note: We are using GPT-2 from the openai-community/gpt2 for deploying this project as it's lighter as compared to LLAMA 3. Another reason for using it instead is because its not possible to load model shard checkpoints when streaming an application using streamlit. You can use an inference API to solve this issue, however you require a paid huggingface subscription.
- If the streamed application does not work as intended/shows an error code (which is highly likely considering the fact that I am not using paid subscriptions for either accessing the models or deploying the application as well as i am not using a dedicated database to store the images and the audio files generated), feel free to contact me via my email or my socials.

## How the project looks/works
https://github.com/vishxrad/image2audiostory/assets/154831195/5b7fee8d-e251-4c21-a7d4-410e2c81a23c

