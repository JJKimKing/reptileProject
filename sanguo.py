from urllib.parse import urlparse, parse_qs

import requests
from bs4 import BeautifulSoup
import re



def parse_content(page_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
    }
    url = f'https://www.cuisiliu.net/book/UwEEAlk/{page_id}.html'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    content = response.content.decode()
    soup = BeautifulSoup(content, 'lxml')
    content_note = soup.find(attrs={'class': 'content'})
    if content_note:
        p_tags  = soup.select_one('article.content').get_text(strip=True)
        #遍历所有的<p>标签，并输出其内容
        with open('a.txt', 'a') as fp:
            fp.write(p_tags + "\n")
            fp.write("\n")
    else:
        return

    # 解析链接递归打印
    # 找到下一页的跳转链接
    next_url_tags = soup.find_all('a', text=re.compile('下一页|下一章'))
    if next_url_tags:
        for url_tag in next_url_tags:
            href = url_tag.get('href')
            match = re.search(r'/book/UwEEAlk/([\w\d]+)\.html', href)
            if(match):
                chapter_id = match.group(1)
                print("ID:", chapter_id)
                if chapter_id:
                    parse_content(chapter_id)
                else:
                    print("爬虫完毕")

parse_content(12435495)

