import requests

url = 'https://www.sogou.com/web'
# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

kw = input("enter a keyWord:")
params = {
    'query': kw
}

repsonse = requests.get(url, headers=headers, params=params)
page_text = repsonse.text
page_name = kw + ".html"
with open(page_name, 'w', encoding='utf-8') as f:
     f.write(page_text)
f.close()