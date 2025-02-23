from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

# Load pre-trained model and tokenizer (for demo purposes)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

# Sample FAQ dataset
faq_data = {
    "hours": "We're open 9-5 weekdays. Men should come during business hours.",
    "password": "He can reset his password using the forgot password link.",
    "contact": "She should email support@company.com for help."
}

def detect_and_correct_bias(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    
    # Simple bias correction (demo purposes)
    corrected = text.replace(" he ", " they ").replace("He ", "They ")\
                   .replace(" she ", " they ").replace("She ", "They ")
    return corrected, logits.argmax().item() == 1

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Find best FAQ match (simplified)
        best_match = next((v for k,v in faq_data.items() if k in request.message.lower()), 
                        "I don't know that. Please contact support.")
        
        # Bias detection and correction
        response, is_biased = detect_and_correct_bias(best_match)
        
        return {
            "response": response,
            "was_debiased": is_biased,
            "original": best_match
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Chatbot API is running"}