# Mock-API

first run this command
uvicorn app:app --host 0.0.0.0 --port 10000

then this,
curl -X POST http://localhost:10000/predict -H "Content-Type: application/json" -d "{}"
or simply use postman
