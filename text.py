import json
import urllib

import requests
from bs4 import BeautifulSoup




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
}

response = requests.get('http://www.baidu.com', headers=headers)
response.encoding = 'utf-8'
content = response.content.decode()
soup = BeautifulSoup(response.content.decode(), 'lxml')

text_list = soup.find_all(attrs={'class': 'title-content-title'})

textarea_element = soup.find('textarea', id='hotsearch_data')
if textarea_element:
    # 获取JSON字符串
    json_str = textarea_element.text

    # 解码URL编码
    json_str_decoded = urllib.parse.unquote(json_str)

    # 将JSON字符串解析为Python字典
    json_data = json.loads(json_str_decoded)

    # 打印解析得到的数据
    hot_search_data = json_data.get('hotsearch', [])

    for temp_json_data in hot_search_data:
        print(temp_json_data.get('card_title', ''))
