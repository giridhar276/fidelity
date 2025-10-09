# 11_get_products_with_auth.py
# Logs in to obtain a token, then performs an authorized GET
import requests, json
BASE = "https://fakestoreapi.com"
creds = {"username": "mor_2314", "password": "83r5^_"}
auth = requests.post(f"{BASE}/auth/login", json=creds, timeout=20).json()
token = (auth or {}).get("token")
headers = {"Authorization": f"Bearer {token}"} if token else {}
r = requests.get(f"{BASE}/products", params={"limit": 3}, headers=headers, timeout=20)
print("Auth token present:", bool(token))
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))