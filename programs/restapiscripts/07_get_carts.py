# 07_get_carts.py
import requests, json
BASE = "https://fakestoreapi.com"
r = requests.get(f"{BASE}/carts", timeout=20)
print("Status:", r.status_code)
data = r.json()
print("Carts:", len(data))
print(json.dumps(data[:2], indent=2))