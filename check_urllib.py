#encoding : utf-8
from urllib import request
import http.cookiejar

url = 'http://www.baidu.com'

print('第一种方法：')
response1 = request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('第二种方法：')
rst = request.Request(url)
#伪装成浏览器访问
rst.add_header('user-agent', 'Mozilla/5.0')
response2 = request.urlopen(url)
print(response2.getcode())
print(len(response2.read()))

print('第三种方法：')
#增加cookie的处理
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(len(response3.read()))
print(cj)