# 15_delete_product.py
# pip install requests
import requests, json

BASE = "https://fakestoreapi.com"

# 1) Create, so we have an id to delete
seed_resp = requests.post(
    f"{BASE}/products",
    json={
        "title": "Delete Me",
        "price": 10.0,
        "description": "Temp",
        "image": "https://i.pravatar.cc",
        "category": "men's clothing",
    },
    timeout=20,
)
print("Seed status:", seed_resp.status_code, "| content-type:", seed_resp.headers.get("content-type"))
try:
    seed_json = seed_resp.json()
except ValueError:
    seed_json = {"raw": seed_resp.text[:300]}
print("Seed body (compact):", json.dumps(seed_json, indent=2)[:400])

pid = (seed_json or {}).get("id") or 7

# 2) Delete
del_resp = requests.delete(f"{BASE}/products/{pid}", timeout=20)
print("Delete status:", del_resp.status_code, "| content-type:", del_resp.headers.get("content-type"))

# Some FakeStore endpoints return non-JSON or empty body for DELETE; handle both safely
try:
    body = del_resp.json()
    print("Delete JSON:\n", json.dumps(body, indent=2))
except ValueError:
    text = del_resp.text.strip()
    if text:
        print("Delete raw text (not JSON):\n", text[:400])
    else:
        print("Delete body is empty (common for 200/204).")
