from fastapi import FastAPI, Request
from model import model

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
    data = await request.json()
    output = model.predict(data)
    return output
