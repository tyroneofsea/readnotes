import requests
from settings import *
import random

class BookInitSpider(object):
    def __init__(self):
        self.url = 'https://www.biquge.com.cn/'
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


    def get_spider_urls(self):
        self.set_headers(self.target_url[1])
        print(self.target_url[1])
        print(self.headers)
        try:
            res = requests.get(url=self.target_url[1], headers=self.headers)
            print(res.code_status)
        except:
            res = None

        if res is None:
            self.set_headers(self.target_url[1])
            try:
                res = requests.get(url=self.target_url[1], headers=self.headers)
                print(res.code_status)
            except:
                res = None
        if res is None:
            print("什么情况？")
            return 2 # "读取文章分类失败" continue

        print(res.text)



    def run(self):  # 实现主要逻辑
        self.get_spider_urls()


if __name__ == '__main__':
    bookinitspider = BookInitSpider()
    result = bookinitspider.run()
    if result == 1:
        print("读取cookies失败，检查网络状况")
