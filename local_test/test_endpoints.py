import requests

def test_ping():
    response = requests.get('http://localhost:8080/ping')
    print(f"Ping response (Status {response.status_code}):", response.text)

if __name__ == "__main__":
    print("Testing /ping endpoint...")
    test_ping()
    print("Testing complete.")