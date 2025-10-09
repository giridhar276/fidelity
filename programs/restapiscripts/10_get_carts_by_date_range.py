# 10_get_carts_by_date_range.py
import requests, json
BASE = "https://fakestoreapi.com"
params = {"startdate": "2019-12-10", "enddate": "2020-10-10"}
r = requests.get(f"{BASE}/carts", params=params, timeout=20)
print("Status:", r.status_code)
print(json.dumps(r.json(), indent=2))