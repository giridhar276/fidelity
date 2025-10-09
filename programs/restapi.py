

# pip install requests
import requests, json

BASE = "https://fakestoreapi.com"

print("\n1) GET all products (limit=5)")
r = requests.get(f"{BASE}/products", params={"limit": 5}, timeout=20)
products = r.json()
print("count:", len(products))
print(json.dumps(products[:2], indent=2)[:600], "...")

print("\n2) GET single product (id=1)")
r = requests.get(f"{BASE}/products/1", timeout=20)
p1 = r.json()
print("title:", p1.get("title"))
print(json.dumps(p1, indent=2)[:300], "...")

print("\n3) GET categories")
r = requests.get(f"{BASE}/products/categories", timeout=20)
cats = r.json()
print("categories:", cats)

print("\n4) GET products in category = 'jewelery' (first 2)")
r = requests.get(f"{BASE}/products/category/jewelery", timeout=20)
jewel = r.json()
print(json.dumps(jewel[:2], indent=2))

print("\n5) GET with params (limit=3 & sort=desc)")
r = requests.get(f"{BASE}/products", params={"limit": 3, "sort": "desc"}, timeout=20)
print(json.dumps(r.json(), indent=2))

print("\n6) CREATE product (POST)")
new_product = {
    "title": "Blue Cap",
    "price": 199.99,
    "description": "Lightweight blue cap",
    "image": "https://i.pravatar.cc",
    "category": "men's clothing"
}
r = requests.post(f"{BASE}/products", json=new_product, timeout=20)
created = r.json()
print("Created:", json.dumps(created, indent=2))
created_id = created.get("id")

print("\n7) UPDATE product (PUT) — using the created id if available")
update_id = created_id if created_id else 7
r = requests.put(f"{BASE}/products/{update_id}",
                 json={"title": "Blue Cap (Updated)", "price": 149.50},
                 timeout=20)
updated = r.json()
print("Updated:", json.dumps(updated, indent=2))

print("\n8) DELETE product — same id")
r = requests.delete(f"{BASE}/products/{update_id}", timeout=20)
print("Delete response:", json.dumps(r.json(), indent=2))

print("\n9) AUTH: login to get a token")
creds = {"username": "mor_2314", "password": "83r5^_"}
r = requests.post(f"{BASE}/auth/login", json=creds, timeout=20)
token = r.json().get("token")
print("Token head:", (token[:20] + "...") if token else "No token returned")

headers = {"Authorization": f"Bearer {token}"} if token else {}

print("\n10) GET products with Authorization header (limit=3)")
r = requests.get(f"{BASE}/products", params={"limit": 3}, headers=headers, timeout=20)
print(json.dumps(r.json(), indent=2))

print("\n11) USERS: list first 2 and single user (id=1)")
r = requests.get(f"{BASE}/users", timeout=20)
users = r.json()
print("Total users fetched:", len(users))
print("First user compact:", {"id": users[0].get("id"), "email": users[0].get("email")} if users else {})
r = requests.get(f"{BASE}/users/1", timeout=20)
print("User #1:", json.dumps(r.json(), indent=2))

print("\n12) CARTS: list first 2")
r = requests.get(f"{BASE}/carts", timeout=20)
carts = r.json()
print(json.dumps(carts[:2], indent=2))

print("\n13) CREATE cart (POST)")
cart_payload = {
    "userId": 3,
    "date": "2020-02-03",
    "products": [
        {"productId": 5, "quantity": 2},
        {"productId": 1, "quantity": 1}
    ]
}
r = requests.post(f"{BASE}/carts", json=cart_payload, timeout=20)
created_cart = r.json()
print("Created cart:", json.dumps(created_cart, indent=2))
cart_id = created_cart.get("id")

print("\n14) UPDATE cart (PUT) — add one more item if id exists")
if cart_id:
    updated_cart_payload = {
        "userId": 3,
        "date": "2020-02-04",
        "products": [
            {"productId": 5, "quantity": 2},
            {"productId": 1, "quantity": 1},
            {"productId": 2, "quantity": 1}
        ]
    }
    r = requests.put(f"{BASE}/carts/{cart_id}", json=updated_cart_payload, timeout=20)
    print("Updated cart:", json.dumps(r.json(), indent=2))
else:
    print("No cart id returned; skipping PUT.")

print("\n15) DELETE cart — same id (if exists)")
if cart_id:
    r = requests.delete(f"{BASE}/carts/{cart_id}", timeout=20)
    print("Delete cart response:", json.dumps(r.json(), indent=2))
else:
    print("No cart id to delete; skipping DELETE.")

print("\nDONE. (Note: FakeStore write operations are mock and may not persist.)")
