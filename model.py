import json
from pathlib import Path

class MockModel:
    def __init__(self):
        json_path = Path(__file__).parent / "response.json"
        with open(json_path, "r") as f:
            self.response = json.load(f)

    def predict(self, data):
        return self.response

model = MockModel()
