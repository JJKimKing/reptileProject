import requests
from bs4 import BeautifulSoup

url = 'https://useragentstring.com/pages/useragentstring.php?name=Chrome'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
user_agents = []
response = requests.get(url, headers=headers)
if response.status_code == 200:
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    ua_list = soup.find_all('ul')
    for ua_link in ua_list:
        h4_tag = ua_link.find_previous_sibling('h4')
        ua_li_tag = ua_link.find('li')
        if h4_tag is not None and ua_li_tag is not None:
            name = h4_tag.text
            ua_agent = ua_li_tag.text
            user_agents.append({name: ua_agent})

if len(user_agents) > 0:
    for ua in user_agents:
        for key, value in ua.items():
            with open('user_agents.txt', 'a') as f:
                f.write(key + '=' + value + '\n')
