import requests  


headers = {'Authorization': 'Token e510903362b4cd9bdf67fa28a683d697eb3b0d8b'}

endpoint = 'http://localhost:9000/api/products/'
r = requests.post(endpoint, headers=headers,json={"title": "apply preform create", "price":1500})

print(r.json())
