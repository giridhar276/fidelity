# 01_get_products.py
# pip install requests
import requests, json
BASE = "https://fakestoreapi.com"
r = requests.get(f"{BASE}/products",auth=("user","password"), params={"limit": 5, "sort": "desc"}, timeout=20)
print("Status:", r.status_code)
print("Count:", len(r.json()))
print(json.dumps(r.json()[:2], indent=2))




