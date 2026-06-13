import requests

params = {
    "shouji": "13456755448",
    "appkey": "0c818521d38759e1"
}
r = requests.post('https://api.binstd.com/shouji/query', params=params)
print(r.status_code)
print(r.json())
