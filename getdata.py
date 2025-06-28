import requests

response = requests.get(" https://7ed8-2a09-bac5-3b5a-7eb-00-ca-15f.ngrok-free.app/get_records")
print(response.json())