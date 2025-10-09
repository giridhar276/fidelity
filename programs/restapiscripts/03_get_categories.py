# 03_get_categories.py
import requests, json
BASE = "https://fakestoreapi.com"
r = requests.get(f"{BASE}/products/categories", timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))