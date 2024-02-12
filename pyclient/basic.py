import requests  


# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/"


# res = requests.get(endpoint)

# print(res.text)
# print(res.json())
# import requests
# r = requests.get('https://httpbin.org/anything', auth=('user', 'pass'), data={"hello": "world"})
endpoint = 'http://localhost:8000/api/'
r = requests.post('http://localhost:8000/api/',  json={ "title":"phone", "price" : 1000,"content": "iphone 15"})
# r = requests.get('http://localhost:8000/api/', params={"abc": 123}, data={"query": "hiiiiii"})
# print(r.headers)    
# print(r.status_code)
# 200
# print(r.headers['content-type'])
# 'application/json; charset=utf8'
# print(r.encoding)
# 'utf-8'
# print(r.text)
# '{"authenticated": true, ...'
print(r.json())
# print(r.json())
# {'authenticated': True, ...}