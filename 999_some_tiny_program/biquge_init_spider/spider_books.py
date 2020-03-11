import requests
from settings import *


class BookSpider(object):
    def __init__(self):
        self.target_url = MAIN_TAGET_URL

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

    def run(self):
        for i in range(0, len(self.target_url)):
            if i == 8:
                book_class = MAIN_TAGET_TITLES[i]
                book_infos_list = self.get_spider_urls(self.target_url[i])
                for book_infos_url in book_infos_list:
                    
            else:
                book_class = MAIN_TAGET_TITLES[i]
                book_infos_list = self.get_normal_urls(self.target_url[i])
