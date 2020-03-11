# import http.cookiejar
# import urllib.request
#
# url = "https://www.biquge.com.cn/quanben/"
# fileName = 'cookie.txt'
#
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open(url)
#
# f = open(fileName,'a')
# for item in cookie:
#     f.write(item.name+" = "+item.value+'\n')
# f.close()
#
import http.cookiejar
import urllib.request

url = "https://www.biquge.com.cn/quanben/"

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open(url)
print(cookie)

for item in cookie:
    print(item.name+" = "+item.value)
