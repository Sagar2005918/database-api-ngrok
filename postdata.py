import requests

data = {
    "user_name": "Sagar",
    "exercise": "Bench Press",
    "weight": 70,
    "reps": 10,
    "record_date": "2025-06-28"
}

response = requests.post("https://7ed8-2a09-bac5-3b5a-7eb-00-ca-15f.ngrok-free.app/add_record", json=data)
print(response.json())
