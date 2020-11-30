import requests
import json

# GET request
r = requests.get("http://127.0.0.1:5000/")
json_resp = json.loads(r.text)
json_resp

# POST request
data = {"1": "Stanislava H", "2": "Juan P", "3":"Cariza M"}
headers = {"Content-Type": "application/json"}
r = requests.post("http://127.0.0.1:5000/", params=data, headers=headers)
json_resp = json.loads(r.text)
json_resp

# DELETE request
data = {"1": "Stanislava H"}
headers = {"Content-Type": "application/json"}
r = requests.delete("http://127.0.0.1:5000/", params=data, headers=headers)
json_resp = json.loads(r.text)
json_resp