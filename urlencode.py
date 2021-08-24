from urllib import parse

data = {'name':'LaoWang', 'age':18, 'greet':'Hello World'}

qs = parse.urlencode(data)
print(qs)
print(parse.parse_qs(qs))

from urllib import request

# %E9%98%BF%E4%BF%A1
url = 'https://cn.bing.com/search?q='

data = {'axin':'阿信'}

qs2 = parse.urlencode(data)

resp = request.urlopen(url + qs2)

print(resp)
# print(resp.read())

# 不用字典，用字符串编码
str01 = '阿信'

str02 = parse.quote(str01)

print(str02)