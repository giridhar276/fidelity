# 06_get_user_by_id.py
import requests, json
BASE = "https://fakestoreapi.com"
uid = 1
r = requests.get(f"{BASE}/users/{uid}", timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))