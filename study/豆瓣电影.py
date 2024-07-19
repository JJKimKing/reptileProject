import json

import requests

url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
params = {
    "type": 11,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
req = requests.get(url, headers=headers, params=params)
page_json = req.json()
print(page_json)

f = open('douban.json', 'w', encoding='utf-8')
json.dump(page_json, fp=f, ensure_ascii=False, indent=4)
