'''
page = urllib2.urlopen(url)
charset = page.headers['Content-Type'].lower().split("charset=")[1]
content = page.read().decode(charset, "ignore").encode("utf-8",'ignore')
soup = BeautifulSoup(content)

title = soup.title.string
description = soup.find(attrs={"name":"description"})['content']
keywords = soup.find(attrs={"name":"keywords"})['content']


注意有的网站并没有这两个信息，有时网站的keywords不为小写。

user_agent = {'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400 QQBrowser/9.7.12661.400'}
header = {'User-Agent':user_agent}
'''
import requests
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400 QQBrowser/9.7.12661.400'
headers = {'User-Agent':user_agent}
url = 'http://hnaepi.com/'
res = requests.get(url=url, headers=headers)
res.encoding = 'utf8'
print(type(res))
print(res.status_code)


soup = BeautifulSoup(res.text, "html.parser")
title = soup.title
print(type(title))
print(title)
description = soup.find(attrs={"name":"description"})['content']
print(description)
keywords = soup.find(attrs={"name":"keywords"})['content']
print(keywords)
