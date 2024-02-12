import requests  



endpoint = 'http://localhost:8000/api/'
r = requests.get('http://localhost:9000/api/products/1/')

print(r.json())
