# 04_get_products_by_category.py
import requests, json
BASE = "https://fakestoreapi.com"
category = "jewelery"
r = requests.get(f"{BASE}/products/category/{category}", timeout=20)
print("Status:", r.status_code)
data = r.json()
print("Count:", len(data))
print(json.dumps(data[:3], indent=2))