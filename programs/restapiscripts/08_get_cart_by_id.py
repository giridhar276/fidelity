# 08_get_cart_by_id.py
import requests, json
BASE = "https://fakestoreapi.com"
cid = 1
r = requests.get(f"{BASE}/carts/{cid}", timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))