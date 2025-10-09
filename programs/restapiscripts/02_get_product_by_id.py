# 02_get_product_by_id.py
import requests, json
BASE = "https://fakestoreapi.com"
pid = 1
r = requests.get(f"{BASE}/products/{pid}", timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))