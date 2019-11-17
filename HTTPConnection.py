from http.client import HTTPConnection


mc = HTTPConnection('www.baidu.com:80')
mc.request('GET', '/')
res = mc.getresponse()


print(res.status, res.reason)
print(res.read().decode('utf-8'))
