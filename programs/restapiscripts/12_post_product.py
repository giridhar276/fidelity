# 12_post_product.py
import requests, json
BASE = "https://fakestoreapi.com"
payload = {
    "title": "Blue Cap",
    "price": 199.99,
    "description": "Lightweight blue cap",
    "image": "https://i.pravatar.cc",
    "category": "men's clothing"
}
r = requests.post(f"{BASE}/products", json=payload, timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))