import os, io
from gtts import gTTS
import streamlit as st
from google import genai
from dotenv import load_dotenv


# Loading environment variable
load_dotenv() 

my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = my_api_key)


# Note generate 
def note_generator(images):
    prompt = """Summarize the picture in note formate at max 100 words
    make sure to add necessary markdown to differentiate difference section"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text

# Audio
def audio_transcription(txt):
    speech = gTTS(txt, lang="en", slow=False)
    audio_buff = io.BytesIO()
    speech.write_to_fp(audio_buff)
    return audio_buff

# Quiz
def quiz_generator(images, diff):
    prompt = f"Generate 3 quizzes based on the {diff}. make sure to add necessary markdown to differentiate difference section"

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text