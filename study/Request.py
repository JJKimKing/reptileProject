import requests

url = 'https://wz.sun0769.com/political/index/politicsNewest'
response = requests.get(url)
html = response.text
with open('politicsNewest.html', 'w') as f:
    f.write(html)
f.close()
