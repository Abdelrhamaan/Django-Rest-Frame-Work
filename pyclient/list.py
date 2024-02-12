import requests  
from getpass import getpass
# endpoint = 'http://localhost:9000/api/products/'
# r = requests.get(endpoint)  

# print(r.json())

user_name = 'admin'
password = getpass()


endpoint = 'http://localhost:9000/api/products/'
auth_endpoint = 'http://localhost:9000/api/auth/'
headers = {'content-type': 'application/json'}

user_name = 'admin'
password = getpass()

auth_endpoint = 'http://localhost:9000/api/products/auth/'
r = requests.post(auth_endpoint, json={'username': 'admin', 'password': password})

if r.status_code == 200:
    token = r.json()['token']
    headers = {'Authorization': f'Token {token}'}
    auth_endpoint = 'http://localhost:9000/api/products/'
    r = requests.get(auth_endpoint, json={'username': 'admin', 'password': password}, headers=headers)
    print('token :' f'{token}')

print(r.json())

