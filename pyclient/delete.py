import requests  

product_id = input("what is th id that you want to delete ")

try:
    product_id = int(product_id)
except :
    product_id = None
    print("Product id is not right id ")
if product_id :
    endpoint = f'http://localhost:9000/api/products/{product_id}/delete/'
r = requests.delete(endpoint)

print(r.status_code)
