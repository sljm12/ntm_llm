import os
import google.generativeai as genai
from openai_llm import prompt_template, extract_json
from dotenv import load_dotenv

load_dotenv()

def call_llm(text):
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat()

    response = chat_session.send_message(prompt_template.format(text=text))
    return extract_json(response.text)