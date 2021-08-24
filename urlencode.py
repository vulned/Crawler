from urllib import parse

data = {'name':'LaoWang', 'age':18, 'greet':'Hello World'}

qs = parse.urlencode(data)
print(qs)
print(parse.parse_qs(qs))

from urllib import request

# 阿信 = %E9%98%BF%E4%BF%A1
url = 'https://cn.bing.com/search?q='

data = {'axin':'阿信'}

qs2 = parse.urlencode(data)
print(qs2)

resp = request.urlopen(url + qs2)
resp02 = request.urlopen(url + parse.quote('阿信'))
print(resp)
print(resp02)
# q=axin=%E9%98%BF%E4%BF%A1 和 q=阿信不同，前者倾向于视频
# print(resp.read())

# 不用字典，用字符串编码
str01 = '阿信'
str02 = parse.quote(str01)
print(str02)