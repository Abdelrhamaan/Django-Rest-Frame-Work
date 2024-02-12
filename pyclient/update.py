import requests  

data = {
    'title' : "i edit the first record",
    'price' : 120,
}

endpoint = 'http://localhost:9000/api/products/1/update/'
r = requests.put(endpoint, json=data)

print(r.json())
