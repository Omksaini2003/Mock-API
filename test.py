import os
import json
import requests

# API_URL = "https://mock-api-wg2l.onrender.com/predict"   
API_URL = "http://localhost:10000/predict"

SAMPLES_DIR = "mock requests samples"              # folder containing your JSON files

def load_json_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith(".json")]
    for filename in files:
        path = os.path.join(directory, filename)
        with open(path, "r") as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"[ERROR] Failed to parse JSON in {filename}: {e}")
                continue
        yield filename, data


def send_request(name, data):
    print(f"\n=== Testing {name} ===")
    try:
        response = requests.post(API_URL, json=data)
        print("Status:", response.status_code)
        print("Response:")
        print(response.json())
    except Exception as e:
        print("[ERROR] Request failed:", e)


def main():
    if not os.path.exists(SAMPLES_DIR):
        print(f"[ERROR] Folder '{SAMPLES_DIR}' not found!")
        return

    for filename, data in load_json_files(SAMPLES_DIR):
        send_request(filename, data)


if __name__ == "__main__":
    main()
