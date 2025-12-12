import json
from fastapi import FastAPI, HTTPException, Request
from model import model
from request_model import PredictRequest

app = FastAPI(
    title="ML Mock API",
    description="Temporary mock server to unblock frontend/backend integration",
    version="0.0.1"
)



@app.get("/")
def health():
    return {"status": "ok", "message": "mock api running"}

@app.post("/predict")
async def predict(payload: PredictRequest):
    # payload is now validated
    output = model.predict(payload.model_dump_json())
    return output
