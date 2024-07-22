# 爬取文章的标题作为text的名称,内容是对应的正文

import os

import requests
from bs4 import BeautifulSoup


# 获取小说正文
def getContent(url):
    str_list = []
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'lxml')
    p_tag = soup.find_all('p')
    for p in p_tag:
        content = p.get_text().replace('\xa0', ' ')
        str_list.append(content)
    return ''.join(str_list)


if __name__ == '__main__':
    # 创建文件夹
    if not os.path.exists("./sanguo"):
        os.mkdir("./sanguo")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'lxml')
    link_soup = soup.find_all('ul')[2]
    for link in link_soup.find_all('li'):
        a_tag = link.find('a')
        if a_tag is not None:
            title = a_tag.text
            a_link = a_tag.get('href')
            content = getContent('https://www.shicimingju.com/' + a_link)
            with open(f'./sanguo/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(content)
print("爬虫完毕")
