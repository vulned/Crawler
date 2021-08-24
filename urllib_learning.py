from urllib import request

resp = request.urlopen('http://shj.xining.gov.cn/gzdt/hjzf/')

print(resp)

# print(resp.read())
# print(resp.read(10))
# print(resp.readline())
# print(resp.readlines())
print(resp.getcode())