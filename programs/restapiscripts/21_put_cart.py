# 21_put_cart.py
import requests, json
BASE = "https://fakestoreapi.com"
# seed
p = requests.post(f"{BASE}/products", json={
    "title": "Cart PUT Seed","price": 30.0,"description": "Seed","image":"https://i.pravatar.cc","category":"men's clothing"
}, timeout=20).json()
pid = (p or {}).get("id") or 1
u = requests.post(f"{BASE}/users", json={
    "email":"cart.put@example.com","username":"cartput","password":"cartpass",
    "name":{"firstname":"Cart","lastname":"Put"},
    "address":{"city":"Hyd","street":"Rd","number":6,"zipcode":"500001","geolocation":{"lat":"17.4","long":"78.5"}},
    "phone":"91-40-555-0001"
}, timeout=20).json()
uid = (u or {}).get("id") or 1
c = requests.post(f"{BASE}/carts", json={"userId": uid, "date": "2020-02-03", "products":[{"productId": pid, "quantity": 1}]}, timeout=20).json()
cid = (c or {}).get("id") or 1
# PUT
payload = {"userId": uid, "date": "2020-02-04","products":[{"productId": pid, "quantity": 3}]}
r = requests.put(f"{BASE}/carts/{cid}", json=payload, timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))