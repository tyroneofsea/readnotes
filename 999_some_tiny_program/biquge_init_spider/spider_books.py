import requests
from settings import *
import socket
import urllib
import random
from bs4 import BeautifulSoup
import re


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
        print("headers = ", headers)
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
            print(book_info_url["href"])
            return_list.append(book_info_url["href"])
            # self.start_get_info(book_info_url["href"])

        list2 = soup.select('#main #newscontent .r ul li .s2 a')
        for book_info_url in list1:
            print(book_info_url["href"])
            # self.start_get_info(book_info_url["href"], book_class)
            return_list.append(book_info_url["href"])
        if return_list == None:
            return None
        else:
            return return_list

    def is_book_infos_url_in_mongodb(self, url):
        pass

    def get_id_from_url(self, url):
        return re.findall(r"\d+\.?\d*", url)[0]

    def run(self):
        for i in range(0, len(self.target_url)):
            if i == 8:
                # 目标域名列表
                book_class = MAIN_TAGET_TITLES[i]
                # 获取首页域名列表
                book_infos_list = self.get_spider_urls(self.target_url[i])
                for book_infos_url in book_infos_list:
                    # 获取图书首页的列表
                    print(book_infos_url)
                    book_id = self.get_id_from_url(book_infos_url)
                    print(book_id)
                    # 判断首页列表是否存在于book_infos中
                    # is_book_infos_url_in_mongodb(book_infos_url)

            else:
                book_class = MAIN_TAGET_TITLES[i]
                book_infos_list = self.get_normal_urls(self.target_url[i])
                for book_infos_url in book_infos_list:
                    # 获取图书首页的列表
                    print(book_infos_url)
                    book_id = self.get_id_from_url(book_infos_url)
                    print(book_id)
                    # 判断首页列表是否存在于book_infos中
                    # is_book_infos_url_in_mongodb(book_infos_url)

def main():
    book = BookSpider()
    book.run()


if __name__ == '__main__':
    main()
