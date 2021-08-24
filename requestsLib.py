import requests

url = 'https://www.baidu.com/'
# 案例一
resp = requests.get(url)
print(resp.cookies)
print('-------------------------------')
print(resp.cookies.get_dict)
print('-------------------------------')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
}

resp = requests.post(url, headers=headers)
# 
print(resp.content)
print('-------------------------------')
print(resp.content.decode('utf-8'))