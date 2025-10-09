# 13_put_product.py
import requests, json
BASE = "https://fakestoreapi.com"
# seed a product first so we have an id
seed = requests.post(f"{BASE}/products", json={
    "title": "Seed Cap","price":50.0,"description":"Seed","image":"https://i.pravatar.cc","category":"men's clothing"
}, timeout=20).json()
pid = (seed or {}).get("id") or 7
r = requests.put(f"{BASE}/products/{pid}", json={"title": "Seed Cap (PUT)", "price": 55.5}, timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))