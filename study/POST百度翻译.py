import requests
import json

url = 'https://fanyi.baidu.com/sug'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
kw = input("enter keyword:")
data = {
    'kw': kw,
}
rep = requests.post(url, headers=header, data=data)
# 只有返回的是json类型才可以用.json()
rep_json = rep.json()
page_name = kw + '.json'
with open(page_name, 'w', encoding='utf-8') as f:
    f.write(json.dumps(rep_json, ensure_ascii=False))
f.close()
