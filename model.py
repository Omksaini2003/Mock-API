class MockModel:
    def __init__(self):
        pass

    def predict(self, data):
        # Always returns the same mock result
        return {
            "prediction": "mock_output",
            "confidence": 0.55,
            "model_version": "0.0.1-mock"
        }


# Create a global instance
model = MockModel()
