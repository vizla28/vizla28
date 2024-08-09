# Create a Pydantic model for the JSON body that contains a single field called 'text'
# Create a FastAPI endpoint that accepts a POST request with a JSON body containing 'text' and returns a checksum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Pydantic model
class TextRequest(BaseModel):
    text: str

@app.post("/checksum")
def get_checksum(request: TextRequest):
    # Compute checksum
    checksum = hashlib.sha256(request.text.encode()).hexdigest()
    return {"checksum": checksum}
@app.get("/")
def read_root():
    return {"message": "Welcome to the API! Developed by [Your Name]"}
"""
@app.post("/checksum")
- **Request Body:**
  - **text:** (string) The text for which the checksum needs to be generated.
- **Response:**
  - **checksum:** (string) The SHA-256 checksum of the provided text.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_checksum():
    response = client.post("/checksum", json={"text": "test"})
    assert response.status_code == 200
    assert "checksum" in response.json()
