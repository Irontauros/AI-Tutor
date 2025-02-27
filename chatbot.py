import ollama

def get_german_response(user_input: str) -> str:
    try:
        response = ollama.chat(
            model="llama3",  # Change model if needed
            messages=[{"role": "user", "content": user_input}]
        )
        return response["message"]["content"]
    except Exception as e:
        return str(e)
