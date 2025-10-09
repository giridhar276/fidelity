# 20_post_cart.py
import requests, json
BASE = "https://fakestoreapi.com"
# ensure a product and user exist
p = requests.post(f"{BASE}/products", json={
    "title": "Cart Seed","price": 20.0,"description": "Seed","image":"https://i.pravatar.cc","category":"men's clothing"
}, timeout=20).json()
pid = (p or {}).get("id") or 1
u = requests.post(f"{BASE}/users", json={
    "email":"cart.user@example.com","username":"cartuser","password":"cartpass",
    "name":{"firstname":"Cart","lastname":"User"},
    "address":{"city":"Hyd","street":"Rd","number":5,"zipcode":"500001","geolocation":{"lat":"17.4","long":"78.5"}},
    "phone":"91-40-555-0000"
}, timeout=20).json()
uid = (u or {}).get("id") or 1
payload = {"userId": uid, "date": "2020-02-03", "products":[{"productId": pid, "quantity": 2}]}
r = requests.post(f"{BASE}/carts", json=payload, timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))