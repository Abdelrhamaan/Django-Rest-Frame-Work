import requests  



# endpoint = 'http://localhost:8000/api/products/'
# r = requests.post(endpoint, json={"title": "lab", "price":1500})

# print(r.json())



# import requests  



# endpoint = 'http://localhost:8000/api/products/'
# r = requests.get(endpoint)  

# print(r.json())


# import requests  



endpoint = 'http://localhost:8000/api/'
r = requests.get('http://localhost:8000/api/products/1/')

print(r.json())
