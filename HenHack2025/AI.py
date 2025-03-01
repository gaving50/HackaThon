import os
from dotenv import load_dotenv
from google import genai


def get_gemini_api_key():
     load_dotenv()
     api_key = os.getenv('GEMINI_API_KEY')
     if not api_key:
         raise ValueError("No Gemini API key found. Please set the GEMINI_API_KEY environment variable.")
     return api_key

def make_gemini_request(user_input):
     api_key = get_gemini_api_key()
     client = genai.Client(api_key=api_key)
     response = client.models.generate_content(
         model="gemini-2.0-flash", contents=user_input)
     if not response:
         raise Exception("Request failed.")
     return response