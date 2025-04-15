import requests

URL = "http://127.0.0.1:8000/abc"

d = {'sid':2020148010, 'name':'KIMHALIM'}

r = requests.post(url=URL, data=d)

print(r.status_code)
print(r.text)   