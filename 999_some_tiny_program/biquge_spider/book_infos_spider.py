import requests
import urllib
from bs4 import BeautifulSoup



url = "https://www.biquge.com.cn/book/7889/"
request = urllib.request.urlopen(url=url)
# print(request.headers)
# print(request.read().decode('utf-8'))

html = request.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())


# book_id =
book_infos = soup.select('#wrapper .box_con #maininfo #info')
book_name = soup.select('#wrapper .box_con #maininfo #info h1')[0].text
print(book_name)
book_auhter = soup.select('#wrapper .box_con #maininfo #info p')[0].text
print(book_auhter)
print("---------------------------------------------------------------------------------")
book_st = soup.select('#wrapper .box_con #maininfo #info p')[1].text
status = book_st.split(',')
book_status = status[0]
print(book_status)
print("---------------------------------------------------------------------------------")
book_last_updata_time = soup.select('#wrapper .box_con #maininfo #info p')[2].text
print(book_last_updata_time)
book_last_updata_desc = soup.select('#wrapper .box_con #maininfo #info p')[3].text
print(book_last_updata_desc)
book_last_updata_url = soup.select('#wrapper .box_con #maininfo #info p a')[2].attrs['href']
print(book_last_updata_url)

next_url = soup.select('#wrapper .box_con #list dl dd a')[0].attrs['href']
print(next_url)
print("--------------------------------img_url-------------------------------------------------")
img_url = soup.select('#wrapper .box_con #sidebar #fmimg img')[0].attrs['src']
print(img_url)
print("--------------------------------img_url-------------------------------------------------")
