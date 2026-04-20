import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3"

conversation_history = []

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    payload = {
        "model": MODEL,
        "messages": conversation_history,
        "stream": False
    }
    
    response = requests.post(OLLAMA_URL, json=payload)
    data = response.json()
    
    assistant_message = data["message"]["content"]
    
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message

def generate_dataset(prompt):
    system_prompt = """You are a dataset generator. 
    When given a description, generate realistic data and return ONLY a JSON object.
    No explanation, no markdown, just raw JSON.
    Format: {"columns": ["col1", "col2"], "rows": [[val1, val2], [val1, val2]]}"""
    
    conversation_history.clear()
    conversation_history.append({
        "role": "system", 
        "content": system_prompt
    })
    
    return chat(prompt)