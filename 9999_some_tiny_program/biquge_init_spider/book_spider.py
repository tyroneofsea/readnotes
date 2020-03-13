import requests
import urllib
from bs4 import BeautifulSoup
from settings import *
import random
import re
from book_spider_pymongo import SpiderMongo
import socket
import time


class BookInitSpider(object):
    def __init__(self):
        self.url = 'https://www.biquge.com.cn'
        self.target_url = MAIN_TAGET_URL
        self.headers = USER_HEADERS
        self.timeout = 2
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

    def set_headers(self):
        # cookies = self.get_new_cookies(url)
        # if cookies == None:
        #     return None
        # self.headers['Cookies'] = cookies
        user_agent = USER_AGENTS[random.randint(0, 19)]
        self.headers['User-Agent'] = user_agent
        return self.headers
        # self.headers['Referer'] = url
        # print("在重置之后的headers = ", self.headers)

    def get_proxy(self):
        try:
            res = requests.get(PROXY_POOL_URL)
            if res.status_code == 200:
                return res.text
        except ConnectionError:
            return None

    def get_html_while(self, url):
        use_url = self.url + url
        print("spidering url =========>",  use_url)
        socket.setdefaulttimeout(self.timeout)
        proxy = self.get_proxy()
        if proxy == None:
            print("代理无效，请速度检查代理池！")
            print("代理无效，请速度检查代理池！")
            pass
        else:
            print(proxy)
            proxies = {
                'socket':  proxy,
                'socket5': proxy
            }

            proxy_support = urllib.request.ProxyHandler(proxies)
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
        # 代理设置完毕

        headers = {
            'User-Agent': USER_AGENTS[random.randint(0, 19)]
        }
        # headers获取完毕
        # print("headers = ", headers)
        try:
            req = urllib.request.Request(url=use_url, headers=headers)
            response = urllib.request.urlopen(req)
            html = response.read().decode("utf8")
            # print(html)
            print("获取到html")
            return html
        except:
            print("没有获取到html")
            return None

    def get_html(self, url):
        html = self.get_html_while(url)
        while html == None:
            html = self.get_html_while(url)
            time.sleep(1)
        return html


    def get_book_infos(self, url, book_class, book_id):
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
        img_url = soup.select('#wrapper .box_con #sidebar #fmimg img')[0].attrs['src']
        book_desc = soup.select('#wrapper .box_con #maininfo #intro')[0].text
        # print(book_last_updata_url)
        # book_class = book_class
        # book_id = book_id
        data_for_book_infos = {
            BOOK_ID: book_id,
            INFOS_CLASS: book_class,
            INFOS_NAME: book_name,
            INFOS_AUTHER: book_auhter,
            INFOS_IMG_URL: img_url,
            INFOS_STATUS: book_status,
            INFOS_LAST_UPDATE_TIME: book_last_updata_time,
            INFOS_LAST_UPDATE_DESC: book_last_updata_desc,
            INFOS_LAST_UPDATE_URL: book_last_updata_url,
            INFOS_DECS: book_desc

        }
        # print("-----------------------------下载图片开始---------------------")
        # todo 写入集合即表：book_infos中
        filepath = BOOK_IMG_DIR + '/' + data_for_book_infos[BOOK_ID] + '.jpg'
        # print(filepath)
        # print(data_for_book_infos[INFOS_IMG_URL])
        try:
            urllib.request.urlretrieve(data_for_book_infos[INFOS_IMG_URL], filename=filepath)
            new_img_url = filepath
        except Exception as e:
            print("Error occurred when downloading file, error message:")
            print(e)
            new_img_url = None
        print(new_img_url)
        data_for_book_infos[INFOS_IMG_URL] = new_img_url
        # print('-------------------------------开始插入-----------------------------------')
        # print(BOOK_INFOS)
        # print(data_for_book_infos)
        spidermongo = SpiderMongo()
        spidermongo.insert_data_dabases(BOOK_INFOS_COLLECTION, data_for_book_infos)
        # print('--------------------------------结束插入----------------------------------')
        # 返回第一页地址
        first_url = soup.select('#wrapper .box_con #list dl dd a')[0].attrs['href']
        return first_url

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
            BOOK_ID: book_id,
            DETAILS_NEXT_URL: next_url,
            DETAILS_CAPTER_NUMB: book_capter_numb,
            DETAILS_CAPTER_NAME: book_capter_name,
            DETAILS_CONTENT: book_content
        }
        #todo 将数据写入数据库
        # print('----------------------------开始插入book_details--------------------------------------')
        spidermongo = SpiderMongo()
        spidermongo.insert_data_dabases(BOOK_DETAILS_COLLECTION, data_for_book_details)
        # print('----------------------------结束插入book_details--------------------------------------')
        return next_url

    def start_get_info(self, url_str, book_class):
        # print(url_str)
        book_id = re.findall(r"\d+\.?\d*", url_str)[0]
        # 获得要去爬取的图书的ID
        first_url = self.get_book_infos(url=url_str, book_class=book_class, book_id=book_id)
        # 返回的是第一页地址
        print("I am OK")
        # 查询并记录该小说的ID、书名、作者、状态、最后更新时间、最后一章URL、描述、分类
        # detail_url第一页的内容
        book_capter_numb = 0
        # 定义章节数
        while True:
            next_url = self.get_book_details(first_url, book_id, book_capter_numb)
            book_capter_numb = book_capter_numb + 1
            if url_str == next_url:
                print(url_str,'========================',next_url)
                print("因为最后的地址指向图书首页，所以这本数爬取完毕")
                print("因为最后的地址指向图书首页，所以这本数爬取完毕")
                print("因为最后的地址指向图书首页，所以这本数爬取完毕")
                print("因为最后的地址指向图书首页，所以这本数爬取完毕")
                return
            else:
                print(first_url,'<<<<<<<<<<<<<<<<<<<<<<<<',next_url)
                first_url = next_url
            # 查询并记录该小说的ID、第几章、该章内容
        return True


    def get_spider_urls(self, url, book_class):
        html = self.get_html(url)
        # 传入的是大类的首页地址
        soup = BeautifulSoup(html, 'lxml')
        novelslist2 = soup.select('#main .novelslist2 ul li .s2 a')
        for span in novelslist2:
            print(span.attrs['href'])
            self.start_get_info(span.attrs['href'], book_class)
        return True

    def get_normal_urls(self, url, book_class):
        html = self.get_html(url)
        # 传入的是大类的首页地址
        soup = BeautifulSoup(html, 'lxml')
        list1 = soup.select('#main #newscontent div ul li .s2 a')
        for book_info_url in list1:
            print(book_info_url["href"])
            self.start_get_info(book_info_url["href"], book_class)
        # 
        # list2 = soup.select('#main #newscontent .r ul li .s2 a')
        # for book_info_url in list2:
        #     print(book_info_url["href"])
        #     self.start_get_info(book_info_url["href"], book_class)
        return True

    def run(self):  # 实现主要逻辑
        for i in range(0, len(self.target_url)):
            if i == 8:
                self.get_spider_urls(self.target_url[i], MAIN_TAGET_TITLES[i])
            else:
                self.get_normal_urls(self.target_url[i], MAIN_TAGET_TITLES[i])





if __name__ == '__main__':
    bookinitspider = BookInitSpider()
    result = bookinitspider.run()
