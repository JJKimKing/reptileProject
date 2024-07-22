import os
import random
import re

import requests
import urllib3
from bs4 import BeautifulSoup

# 忽略https的警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

page_params = ''
url = f'https://pic.netbian.com/4kdongman/index{page_params}.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    "Cookie": "zkhanreturnurl=https%3A%2F%2Fpic.netbian.com%2Fe%2Fmember%2Fbuygroup%2F; zkhanmlusername=qq550090172136; zkhanmluserid=7677176; zkhanmlgroupid=1; zkhanmlrnd=goHik862f7OmB8QckQDf; zkhanmlauth=be2cbf2604f4b7f23ae0b4f12f832741; zkhanecookieclassrecord=%2C54%2C53%2C55%2C66%2C"
}

# 创建一个文件夹来存储图片
if not os.path.exists("./picLibs"):
    os.makedirs("./picLibs")

for pageNum in range(1, 3):
    if pageNum != 1:
        page_params = '_' + str(pageNum)
    response = requests.get(url=url, headers=headers, verify=False)
    response.encoding = 'gbk'
    page_text = response.text
    soup = BeautifulSoup(page_text, 'lxml')
    ul_tags = soup.find(attrs={'class': 'slist'}).find_all('a')
    for ul_tag in ul_tags:
        href = ul_tag.get('href')
        # 提取图片id
        img_id = numbers = re.findall(r'\d+', href)[0]
        url_img = ul_tag.find('img').get('alt').split(' ')[0]
        img_name = f'{url_img}_{random.randint(0, 99)}'  # 随机名字,防止重复
        # 请求token获取4K图片地址
        token_url = f'https://pic.netbian.com/e/extend/downpic.php?id={img_id}&t=0.931231'
        img_token_response = requests.get(url=token_url, headers=headers, verify=False)
        if img_token_response.status_code == 200:
            token_json = img_token_response.json()
            pic_path = token_json['pic']
            result_img_url = f'https://pic.netbian.com{pic_path}'
            img_data = requests.get(url=result_img_url, headers=headers).content
            with open(f"./picLibs/{img_name}.jpg", 'wb') as f:
                f.write(img_data)
print("下载成功!")
