# 23_delete_cart.py
import requests, json
BASE = "https://fakestoreapi.com"
# seed
p = requests.post(f"{BASE}/products", json={
    "title": "Cart DEL Seed","price": 25.0,"description": "Seed","image":"https://i.pravatar.cc","category":"men's clothing"
}, timeout=20).json()
pid = (p or {}).get("id") or 1
u = requests.post(f"{BASE}/users", json={
    "email":"cart.del@example.com","username":"cartdel","password":"cartpass",
    "name":{"firstname":"Cart","lastname":"Del"},
    "address":{"city":"Hyd","street":"Rd","number":8,"zipcode":"500001","geolocation":{"lat":"17.4","long":"78.5"}},
    "phone":"91-40-555-0003"
}, timeout=20).json()
uid = (u or {}).get("id") or 1
c = requests.post(f"{BASE}/carts", json={"userId": uid, "date": "2020-02-03", "products":[{"productId": pid, "quantity": 2}]}, timeout=20).json()
cid = (c or {}).get("id") or 1
# DELETE
r = requests.delete(f"{BASE}/carts/{cid}", timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))