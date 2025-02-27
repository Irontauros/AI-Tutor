AI Tutor - Speak & Learn with AI

Project Overview  
This project is a real-time AI-powered tutor that lets users:  
Ask for translations (e.g., "How do you say 'I love coding' in German?")  
Practice pronunciation (AI listens, corrects, and provides feedback)  
Have natural conversations (AI keeps the chat going)  

Key Features (Planned Stages)  

PHASE 1 - Basic Text-Based Chatbot
- Set up a FastAPI backend.  
- Integrate GPT-4 to generate responses.  
- Allow text input & output.  

PHASE 2 - Add Speech-to-Text (Voice Input)  
- Use Whisper API to recognize spoken words.  
- Allow users to speak instead of typing.  

PHASE 3 - Add Text-to-Speech (Audio Responses)  
- Integrate Google TTS or Coqui TTS** for voice replies.  
- Let users hear the AI speaking.  

PHASE 4 - Pronunciation Feedback & Conversation Flow  
- AI corrects your pronunciation.  
- AI continues the conversation naturally.  

PHASE 5 - Mobile App (iOS & Android) 
- Convert to React Native or Flutter for mobile.  

---

Tech Stack  

| Feature                 | Tech / Library                         |
|-------------------------|--------------------------------------|
| **Backend (Server)**    | FastAPI (Python)        |
| **AI Model (Chat)**     | GPT-4         |
| **Speech-to-Text**      | Whisper API           |
| **Text-to-Speech**      | Google TTS, Coqui TTS              |
| **Frontend (Web)**      | React       |
| **Mobile App (Later)**  | React Native             |

---

# Install dependencies
pip install fastapi uvicorn openai

# Run the server
uvicorn main:app --reload
