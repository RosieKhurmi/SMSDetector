import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from server.predict import classify_message
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str


@app.post("/predict/")
def predict(message: Message):
    try:
        result = classify_message(message.text)
        return {"message": message.text, "prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
