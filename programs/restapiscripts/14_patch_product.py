# 14_patch_product.py
import requests, json
BASE = "https://fakestoreapi.com"
seed = requests.post(f"{BASE}/products", json={
    "title": "Seed Patch","price":60.0,"description":"Seed","image":"https://i.pravatar.cc","category":"men's clothing"
}, timeout=20).json()
pid = (seed or {}).get("id") or 7
r = requests.patch(f"{BASE}/products/{pid}", json={"price": 61.0}, timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))