from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

base_dir = os.getenv('BASE_DIR')
script_dir = os.path.abspath(os.path.join(base_dir, 'app', 'scripts'))
sys.path.append(script_dir)

from predict import classify_message

class Message(BaseModel):
    text: str

@app.post("/predict/")
def predict(message: Message):
    try:
        result = classify_message(message.text)
        return {"message": message.text, "prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))