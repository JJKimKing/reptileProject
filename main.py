import requests
from bs4 import BeautifulSoup

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
# url = 'http://www.baidu.com'
res = requests.get(url)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.content.decode(), 'lxml')
title = soup.find('title')
print(title)

# 查找a标签
# a = soup.find("a")
# print(a)

# 查找所有的a标签
# a_list=soup.findAll('a')
#
# for temp in  a_list:
#     print(temp)


# 根据属性查找
# moves=soup.findAll(attrs={'class':'mnav'})
# print(moves)


# 根据文本来查找
text_msg = soup.find(text='维生素C凝胶糖果60粒')
print(text_msg)

# tag name获取标签的名称,
print(text_msg.name)
print(text_msg.text)
