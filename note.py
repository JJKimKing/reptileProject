from urllib.parse import urlparse, parse_qs

import requests
from bs4 import BeautifulSoup



def parse_content(page_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
    }
    url = f'https://read.zongheng.com/chapter/1292756/{page_id}.html'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    content = response.content.decode()
    soup = BeautifulSoup(content, 'lxml')
    content_note = soup.find(attrs={'class': 'content'})
    if content_note:
        p_tags = content_note.find_all('p')

        # 遍历所有的<p>标签，并输出其内容
        with open('a.txt', 'a') as fp:
            for p_tag in p_tags:
                fp.write(p_tag.text+"\n")

    else:
        return

    # 解析链接递归打印
    # 找到下一页的跳转链接
    next_url_tag=soup.find('a',{'data-nextcid':True})
    if next_url_tag:
        href_value = next_url_tag.get('href')
        parsed_url = urlparse(href_value)
        path_parts = parsed_url.path.split('/')
        chapter_id = path_parts[-1].split('.')[0]
        if chapter_id.isdigit():
            parse_content(chapter_id)
        else:
            print("爬虫完毕")

parse_content(74015478)
