# 09_get_carts_by_user.py
import requests, json
BASE = "https://fakestoreapi.com"
uid = 2
r = requests.get(f"{BASE}/carts/user/{uid}", timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))