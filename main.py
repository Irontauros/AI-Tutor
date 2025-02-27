from fastapi import FastAPI
from chatbot import get_german_response
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the AI German Tutor API"}

@app.post("/chat")
def chat(user_input: str):
    response = get_german_response(user_input)
    return {"response": response}
