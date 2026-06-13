import requests

json_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

url = "https://jsonplaceholder.typicode.com/posts"

r = requests.post(url=url, json=json_data)
print(r.status_code)
print(r.json())
