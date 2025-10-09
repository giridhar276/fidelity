# 05_get_users.py
import requests, json
BASE = "https://fakestoreapi.com"
r = requests.get(f"{BASE}/users", timeout=20)
print("Status:", r.status_code)
data = r.json()
print("Users:", len(data))
print(json.dumps(data[:2], indent=2))