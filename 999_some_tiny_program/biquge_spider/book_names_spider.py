import requests
import urllib
from bs4 import BeautifulSoup
import re
'''
测试获取某个分类下的所有图书的首页
没有用代理
没有用cookies
'''


url = "https://www.biquge.com.cn/quanben/"
request = urllib.request.urlopen(url=url)
# print(request.headers)
# print(request.read().decode('utf-8'))

html = request.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
print(soup.find_all(name='span', attrs='s2'))
novelslist2 = soup.select('#main .novelslist2 ul li .s2 a')
print(novelslist2)
print("-------------------------------end-----------------------------------------------------")

for span in novelslist2:
    try:
        print(span.attrs['href'])
        print(re.findall(r"\d+\.?\d*", span.attrs['href'])[0])
    except:
        print("我只能出现一次")
print("------------------------------------------------------------------------------------")
