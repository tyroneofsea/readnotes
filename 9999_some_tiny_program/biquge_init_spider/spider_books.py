import requests
from settings import *
import socket
import urllib
import random
from bs4 import BeautifulSoup
import re
from book_spider_pymongo import SpiderMongo
import time


class BookSpider(object):
    def __init__(self):
        self.target_url = MAIN_TAGET_URL
        self.url = 'https://www.biquge.com.cn'
        self.timeout = 2

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
            time.sleep(0.1)
        return html

    def get_book_details(self, url, book_id, book_capter_numb):
        '''
        传入参数:   详情页地址： url ， 图书id：book_id，图书章节（id）： book_capter_numb
        方法作用:   记录某一章内容
        返回值:     下一张url
        '''
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
        print('----------------------------开始插入book_details--------------------------------------')
        spidermongo = SpiderMongo()
        spidermongo.insert_data_dabases(BOOK_DETAILS_COLLECTION, data_for_book_details)
        print('----------------------------结束插入book_details--------------------------------------')
        return next_url


    def get_book_infos(self, url, book_class, book_id):
        '''
        传入参数:   首页地址： url ，图书分类： book_class， 图书id：book_id
        方法作用:   记录图示基本信息,写入mongdb数据库， 保存图书图片
        返回值:     返回第一页地址
        '''
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
        print(book_id,"+",book_name,"+",book_class)
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


    def start_get_info(self, url_str, book_class):
        '''
        传入参数:   图书首页地址： url_str，图书分类：book_class
        方法作用:   获取第一页内容，并通过第一页内容，反复抓取，直到该图书信息抓取完毕
        返回值:     True 表示成功
        '''
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

    def get_spider_urls(self, url):
        html = self.get_html(url)
        # 传入的是大类的首页地址
        soup = BeautifulSoup(html, 'lxml')
        novelslist2 = soup.select('#main .novelslist2 ul li .s2 a')
        return_list = []
        for span in novelslist2:
            print(span.attrs['href'])
            # self.start_get_info(span.attrs['href'])
            return_list.append(span.attrs['href'])
        if return_list == None:
            return None
        else:
            return return_list

    def get_normal_urls(self, url):
        html = self.get_html(url)
        # 传入的是大类的首页地址
        soup = BeautifulSoup(html, 'lxml')
        return_list = []
        list1 = soup.select('#main #newscontent div ul li .s2 a')
        for book_info_url in list1:
            # print(book_info_url["href"])
            return_list.append(book_info_url["href"])
            # self.start_get_info(book_info_url["href"])
        #
        # list2 = soup.select('#main #newscontent .r ul li .s2 a')
        # for book_info_url in list2:
        #     print(book_info_url["href"])
        #     # self.start_get_info(book_info_url["href"], book_class)
        #     return_list.append(book_info_url["href"])
        if return_list == None:
            return None
        else:
            return return_list

    def update_book_infos_by_book_id(self, url, book_class, book_id):
        '''
        返回值： 最新的url地址
        '''
        book_id = self.get_id_from_url(url)
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        book_st = soup.select('#wrapper .box_con #maininfo #info p')[1].text
        status = book_st.split(',')
        book_status = status[0]
        # print(book_status)
        # print("---------------------------------------------------------------------------------")
        book_last_updata_time = soup.select('#wrapper .box_con #maininfo #info p')[2].text
        book_last_updata_desc = soup.select('#wrapper .box_con #maininfo #info p')[3].text
        book_last_updata_url = soup.select('#wrapper .box_con #maininfo #info p a')[2].attrs['href']

        data_for_book_infos = {
            INFOS_STATUS: book_status,
            INFOS_LAST_UPDATE_TIME: book_last_updata_time,
            INFOS_LAST_UPDATE_DESC: book_last_updata_desc,
            INFOS_LAST_UPDATE_URL: book_last_updata_url
        }
        s = SpiderMongo()
        res = s.update_book_infos_by_book_id(book_id, data_for_book_infos)

    def get_newest_capter_numb_from_mongodb(self, book_id):
        s = SpiderMongo()
        res = s.get_newest_capter_numb_from_mongodb(book_id)
        if len(res) == 0:
            return None
        else:
            return res[0]['book_capter_numb']

    def get_newest_url_from_index(self, index_url):
        html = self.get_html(index_url)
        soup = BeautifulSoup(html, 'lxml')
        book_last_updata_url = soup.select('#wrapper .box_con #maininfo #info p a')[2].attrs['href']
        return book_last_updata_url

    def is_book_id_in_mongodb(self, book_id):
        '''
        参数： book_id: 图书的ID号
        返回： 如果id存在，返回新一章的url地址
              如果id不存在，返回None
        '''
        searchid = SpiderMongo()
        result =  searchid.is_book_id_in_mongodb(book_id)
        if result == None:
            return result
        else:
            return result['book_last_updata_url']


    def get_id_from_url(self, url):
        return re.findall(r"\d+\.?\d*", url)[0]

    def run(self):
        for i in range(0, len(self.target_url)):
            # 目标域名列表
            book_class = MAIN_TAGET_TITLES[i]
            # 获取首页域名列表
            if i == 8:
                books_index_infos_list = self.get_spider_urls(self.target_url[i])
            else:
                books_index_infos_list = self.get_normal_urls(self.target_url[i])
            # books_infos_list 为所有图书首页组成的url_list
            for book_infos_index_url in books_index_infos_list:
                # book_infos_index_url 为单个图书，首页的url
                print(book_infos_index_url)
                book_id = self.get_id_from_url(book_infos_index_url)
                print(book_id)
                # 判断首页列表是否存在于book_infos中
                mongodb_newest_url = self.is_book_id_in_mongodb(book_id)
                if mongodb_newest_url is not None:
                    # 返回不是None，说明数据库中，已经有了这个book的信息
                    # mongodb_newest_url = slef.get_newest_url_from_mongodb(book_id)
                    index_newest_url = self.get_newest_url_from_index(book_infos_index_url)
                    if mongodb_newest_url == index_newest_url:
                        print("该图书"+ book_id +"目前没有更新")
                    else:
                        print("该图书"+ book_id +"目前有有更新")
                        book_capter_numb  = int(self.get_newest_capter_numb_from_mongodb(book_id)) + 1
                        newest_url = self.update_book_infos_by_book_id(book_infos_index_url, book_class, book_id)
                        while True:
                            next_url = slef.get_book_details(mongodb_newest_url, book_id, book_capter_numb)
                            if newest_url == next_url:
                                print("该图书"+ book_id +"更新完毕")
                                break
                            else:
                                book_capter_numb = book_capter_numb + 1
                                mongodb_newest_url = next_url
                else:
                    # 返回为False，说明数据库中，没有这个book的信息
                    print("该图书"+ book_id +"数据库中没有，从头开始抓取")
                    self.start_get_info(book_infos_index_url, book_class)



if __name__ == '__main__':
    book = BookSpider()
    book.run()
