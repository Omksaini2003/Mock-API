import json
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
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
async def predict(request: Request):
    raw = await(request.json())

    try:
        parsed = PredictRequest(**raw)
    except ValidationError:
        return JSONResponse(
            status_code=400,
            content={
                "status": "invalid_request",
                "message": "Request structure is incorrect."
            }
        )

    return model.predict(parsed.model_dump())