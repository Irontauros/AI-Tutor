from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from chatbot import get_german_response
import os

app = FastAPI()

# Ensure Jinja looks in the correct directory
templates = Jinja2Templates(directory=os.path.dirname(__file__))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, user_input: str = Form(...)):  
    response = get_german_response(user_input)
    return templates.TemplateResponse("index.html", {"request": request, "response": response})
