from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from server.predict import classify_message
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a Pydantic model for the request body
class Message(BaseModel):
    text: str

# Define a POST endpoint for predictions
@app.post("/predict/")
# predict takes in a message and returns a JSON response from classify_message
def predict(message: Message):
    try:
        # Classify the message using the imported classify_message function
        result = classify_message(message.text)
        return {"message": message.text, "prediction": result}
    except Exception as e:
        # Raise an HTTPException with a 500 status code if an error occurs
        raise HTTPException(status_code=500, detail=str(e))
