import requests
import urllib
from bs4 import BeautifulSoup



url = "https://www.biquge.com.cn/book/7889/221137.html"
request = urllib.request.urlopen(url=url)
# print(request.headers)
# print(request.read().decode('utf-8'))

html = request.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())

data_for_book_details = {
    "book_id": 123,
    "book_capter_numb": None,
    "book_capter_name": None,
    "book_content": None
}

book_capter_name = soup.select('#wrapper .content_read .box_con .bookname h1')[0].text
print(book_capter_name)
book_content = soup.select('#wrapper .content_read #content')[0].text
print(book_content)
next_url = soup.select('#wrapper .content_read .box_con .bookname .bottem1 a')[2].attrs['href']
print(next_url)
