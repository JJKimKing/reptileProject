import requests
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

place = input('enter the place name:')
file_name = place + '.json'
for page in range(1, 20):
    params = {
        'cname': '',
        'pid': '',
        'keyword': place,  # 查询地点
        'pageIndex': page,  # 查询页码
        'pageSize': '10',  # 每页最多显示10个
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        page_text = response.json()
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(json.dumps(page_text, ensure_ascii=False))
            f.write('\n')
    page = page + 1
print('over!')
