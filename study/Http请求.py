import requests

url = "http://httpbin.org/get"
params = {
    "key1": "value1",
    "key2": "value2"
}
data = requests.get(url, params=params)
print(data.text)

