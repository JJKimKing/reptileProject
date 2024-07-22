import requests
from bs4 import BeautifulSoup

url = 'https://sh.58.com/ershoufang/p{page}/?PGTID=0d30000c-0000-2fda-5e82-3ebe20d11ac9&ClickID=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
}

result = []

def getAllContent(tags):
    info = []
    for p in tags:
        text = p.get_text(strip=True)
        info.append(text)
    return info


for page in range(1, 2):
    url = url.format(page=page)
    res = requests.get(url, headers=headers, verify=False)

    contents = BeautifulSoup(res.text, 'lxml').find_all('div', attrs={'class': 'property-content'})
    for tag in contents:
        p_tags = tag.find_all('p')
        text = getAllContent(p_tags)
        # 实现爬图片,价格,文本title,细节描述等等
        print(text)