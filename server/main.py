import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Ensure the current directory is in sys.path
sys.path.append(os.path.dirname(__file__))

from predict import classify_message

app = FastAPI()


class Message(BaseModel):
    text: str


@app.post("/predict/")
def predict(message: Message):
    try:
        result = classify_message(message.text)
        return {"message": message.text, "prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
