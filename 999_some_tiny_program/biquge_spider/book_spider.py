import requests
import urllib
from bs4 import BeautifulSoup
from settings import *
import random
import re

class BookInitSpider(object):
    def __init__(self):
        self.url = 'https://www.biquge.com.cn'
        self.target_url = MAIN_TAGET_URL
        self.headers = USER_HEADERS
        # print("在初始化的时候的headers = ", self.headers)

    def get_new_cookies(self, url):
        try:
            response = requests.Session().get(self.target_url[1], verify=False)
            print("get_new_cookies=",response.cookies)
            #返回cookiejar对象
            cookiejar = response.cookies
            #转为字典
            cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
            print(cookiedict)
            return cookiedict
        except:
            return None

    def update_cookie(cookiejar, cookie):
        _cookies = requests.cookies
        _cookies.remove_cookie_by_name(cookiejar, 'cookie_name')
        cookiejar.set_cookie(_cookies.create_cookie('cookie_name', cookie, **{'domain': '.example.com'}))

    def set_headers(self, url):
        cookies = self.get_new_cookies(url)
        if cookies == None:
            return None
        self.headers['Cookies'] = cookies
        user_agent = USER_AGENTS[random.randint(0, 19)]
        self.headers['User-Agent'] = user_agent
        self.headers['Referer'] = url
        # print("在重置之后的headers = ", self.headers)

    def get_html(self, url):
        use_url = self.url + url
        print("spidering url =========>",  use_url)
        request = urllib.request.urlopen(url=use_url)
        html = request.read().decode('utf-8')
        return html

    def get_book_infos(self, url, book_class, book_id):
        print("I am in get book infos:", url)
        print("I am in get book infos:", book_class)
        print("I am in get book infos:", book_id)
        print("I am in get book infos:", url)
        print("I am in get book infos:", book_class)
        print("I am in get book infos:", book_id)
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        book_name = soup.select('#wrapper .box_con #maininfo #info h1')[0].text
        # print(book_name)
        book_auhter = soup.select('#wrapper .box_con #maininfo #info p')[0].text
        # print(book_auhter)
        # print("---------------------------------------------------------------------------------")
        book_st = soup.select('#wrapper .box_con #maininfo #info p')[1].text
        status = book_st.split(',')
        book_status = status[0]
        # print(book_status)
        # print("---------------------------------------------------------------------------------")
        book_last_updata_time = soup.select('#wrapper .box_con #maininfo #info p')[2].text
        # print(book_last_updata_time)
        book_last_updata_desc = soup.select('#wrapper .box_con #maininfo #info p')[3].text
        # print(book_last_updata_desc)
        book_last_updata_url = soup.select('#wrapper .box_con #maininfo #info p a')[2].attrs['href']
        # print(book_last_updata_url)
        # book_class = book_class
        # book_id = book_id
        # todo 写入集合即表：book_infos中
        data_for_book_infos = {
            "book_id": book_id,
            "book_name": book_name,
            "book_auhter": book_auhter,
            "book_status": book_status,
            "book_last_updata_time": book_last_updata_time,
            "book_last_updata_desc": book_last_updata_desc,
            "book_last_updata_url": book_last_updata_url,
            "book_class": book_class
        }
        # 返回第一页地址
        first_url = soup.select('#wrapper .box_con #list dl dd a')[0].attrs['href']
        return first_url

    def get_spider_urls(self, url, book_class):
        html = self.get_html(url)
        # 传入的是大类的首页地址
        soup = BeautifulSoup(html, 'lxml')
        novelslist2 = soup.select('#main .novelslist2 ul li .s2 a')
        for span in novelslist2:
            try:
                print(span.attrs['href'])
                book_id = re.findall(r"\d+\.?\d*", span.attrs['href'])[0]
                # 获得要去爬取的图书的ID
                first_url = self.get_book_infos(url=span.attrs['href'], book_class=book_class, book_id=book_id)
                print("I am OK2")
                # 查询并记录该小说的ID、书名、作者、状态、最后更新时间、最后一章URL、描述、分类
                # detail_url第一页的内容
                book_capter_numb = 0
                # 定义章节数
                while True:
                    next_url = self.get_book_details(first_url, book_id, book_capter_numb)
                    book_capter_numb = book_capter_numb + 1
                    if first_url == next_url:
                        break
                    else:
                        first_url = next_url
                # 查询并记录该小说的ID、第几章、该章内容
            except:
                print("我只能出现一次")



    def get_book_details(self, url, book_id, book_capter_numb):
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        book_capter_name = soup.select('#wrapper .content_read .box_con .bookname h1')[0].text
        # print(book_capter_name)
        book_content = soup.select('#wrapper .content_read #content')[0].text
        # print(book_content)
        next_url = soup.select('#wrapper .content_read .box_con .bookname .bottem1 a')[2].attrs['href']
        # print(next_url)
        data_for_book_details = {
            "book_id": book_id,
            "book_capter_numb": book_capter_numb,
            "book_capter_name": book_capter_name,
            "book_content": book_content
        }
        #todo 将数据写入数据库
        print("-------------------------------------------------------------------------")
        print(book_id)
        print(book_capter_numb)
        print(book_capter_name)
        print(book_content)
        print("-------------------------------------------------------------------------")
        return next_url


    def run(self):  # 实现主要逻辑
        for i in range(0, len(self.target_url)):
            if i == 0:
                pass
                # self.get_spider_urls(self.target_url[i], "玄幻小说")
            elif i == 1:
                pass
                # self.get_spider_urls(self.target_url[i], "修真小说")
            elif i == 2:
                pass
                # self.get_spider_urls(self.target_url[i], "都市小说")
            elif i == 3:
                pass
                # self.get_spider_urls(self.target_url[i], "历史小说")
            elif i == 4:
                pass
                # self.get_spider_urls(self.target_url[i], "网游小说")
            elif i == 5:
                pass
                # self.get_spider_urls(self.target_url[i], "科幻小说")
            elif i == 6:
                pass
                # self.get_spider_urls(self.target_url[i], "言情小说")
            elif i == 7:
                pass
                # self.get_spider_urls(self.target_url[i], "其他小说")
            elif i == 8:
                pass
                self.get_spider_urls(self.target_url[i], "完结小说")
            else:
                print("列表错误，请仔细查看settings.py文件")
                return


if __name__ == '__main__':
    bookinitspider = BookInitSpider()
    result = bookinitspider.run()
    if result == 1:
        print("读取cookies失败，检查网络状况")
