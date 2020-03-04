import requests
import random
import time
from bs4 import BeautifulSoup
'''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: BAIDUID=4598A5614DC49B579474B573322C3794:FG=1; SE_LAUNCH=5%3A26385780; delPer=0; H_WISE_SIDS=141002_142063_135847_142208_122158_142115_141125_142019_141838_140853_142514_138878_140989_142918_142390_142779_142285_136862_131861_140174_131246_137745_138165_140324_138883_133847_140259_141941_127969_140065_142907_140595_143056_138425_141009_141191_141926_131423_141706_107318_142345_138596_142271_140367_141103_110085; rsv_i=c6429MaTEvyEgjsiMRH%2FsyZ0S523c14NqeTUffYy6TTkL77fKalL%2Fm1cpjrDbfO5Uher9QSRxYGja1%2BGI2SKVmorTw%2F5lEk; PSINO=7; BIDUPSID=4598A5614DC49B579474B573322C3794; PSTM=1583153681; BD_HOME=0; BD_UPN=123353; BD_CK_SAM=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=30972_1435_21109_30824_22158; H_PS_645EC=b34fSQC0yXmy5A%2BjNvraDpq4o0YkbcXrHWYTw6NvJQikEa1gCDBmRcYuB1I
Host: www.baidu.com
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.122 Chrome/80.0.3987.122 Safari/537.36
'''


class KeywordsSpider(object):
    def __init__(self, keywords):
        self.user_agents = [
            'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
            'Mozilla/5.0 (Android; Tablet; rv:14.0) Gecko/14.0 Firefox/14.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) CriOS/27.0.1453.10 Mobile/10B350 Safari/8536.25',
            'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.9.168 Version/11.52',
            'Opera/9.80 (Windows NT 6.1; WOW64; U; en) Presto/2.10.229 Version/11.62',
            'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML, like Gecko) Version/7.2.1.0 Safari/536.2+',
            'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
            'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        ]
        real_user_agent = self.user_agents[random.randint(0,19)]
        print(real_user_agent)
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, compress',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://www.baidu.com',
            'Connection': 'keep-alive',
            'Cookie': 'BAIDUID=4598A5614DC49B579474B573322C3794:FG=1; H_WISE_SIDS=141002_142063_135847_142208_122158_142115_141125_142019_141838_140853_142514_138878_140989_142918_142390_142779_142285_136862_131861_140174_131246_137745_138165_140324_138883_133847_140259_141941_127969_140065_142907_140595_143056_138425_141009_141191_141926_131423_141706_107318_142345_138596_142271_140367_141103_110085; BIDUPSID=4598A5614DC49B579474B573322C3794; PSTM=1583153681; BD_UPN=123353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=30972_1435_21109_30824_22158; delPer=0; BD_CK_SAM=1; PSINO=7; BD_HOME=0; H_PS_645EC=32edWtE1uWtBItfZc%2B%2BikBd8qIhE1FwrSKmnQgECa3GnHyOoqovC4EV5oDg; BDSVRTM=0',
            'Host': 'www.baidu.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': real_user_agent
        }
        # self.url = url
        self.baidu_url = 'https://www.baidu.com/s?wd='
        self.keywords = keywords
        self.PROXY_POOL_URL = 'http://localhost:5555/random'

    def get_proxy(self):
        try:
            res = requests.get(self.PROXY_POOL_URL)
            if res.status_code == 200:
                return res.text
        except ConnectionError:
            return None

    def get_baidu_cookie(self):
        url = 'https://www.baidu.com'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400 QQBrowser/9.7.12661.400'
        headers = {'User-Agent':user_agent}

        res = requests.Session().get(url=url, headers=headers)
        print("res.cookies = ", res.cookies)
        return res.cookies


    def get_new_headers(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Upgrade-Insecure-Requests': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Cookies': self.get_baidu_cookie(),
            'User-Agent': self.user_agents[random.randint(0,19)]
        }

    def get_info_request(self, url, headers):

        # proxy = self.get_proxy()
        # proxies = {
        #     'http': 'http://' + proxy,
        #     'https': 'https://' + proxy,
        # }
        # page = requests.get(url=url, headers=self.headers, proxies=proxies)
        try:
            page = requests.get(url=url, headers=headers, timeout=10)
        except:
            page =None


        if page == None:
            headers=self.get_new_headers()
            try:
                page = requests.get(url=url, headers=headers, timeout=10)
            except:
                print("这个链接已经失效，请查看")
                return

        page.encoding = 'utf8'
        soup = BeautifulSoup(page.text, "html.parser")
        title = None
        try:
            title = soup.title.string
            print(title)
        except :
            title = None
            print("没有关键词为title的描述")
        print(title)

        description = None
        try:
            description = soup.find(attrs={"name":"description"})['content']
            print(description)
        except :
            description = None
            print("没有关键词为description的描述")
        if description == None:
            try:
                description = soup.find(attrs={"name":"Description"})['content']
                print(description)
            except :
                description = None
                print("没有关键词为description的描述")

        if description == None:
            try:
                description = soup.find(attrs={"name":"DESCRIPTION"})['content']
                print(description)
            except :
                description = None
                print("没有关键词为description的描述")

        keywords = None
        try:
            keywords = soup.find(attrs={"name":"keywords"})['content']
            print(keywords)
        except :
            keywords = None
            print("没有关键词为description的描述")

        if  keywords == None:
            try:
                keywords = soup.find(attrs={"name":"Keywords"})['content']
                print(keywords)
            except :
                keywords = None
                print("没有关键词为description的描述")

        if  keywords == None:
            try:
                keywords = soup.find(attrs={"name":"KEYWORDS"})['content']
                print(keywords)
            except :
                keywords = None
                print("没有关键词为description的描述")

        if title != None and description != None and keywords != None and description != '' and keywords != '':
            context = {
                "title": title,
                "description": description,
                "keywords": keywords
            }
            return context
        else:
            context = None
            return context



    def get_urls_from_baidu(self):
        return_context = []
        for i in range(0, 3):
            url = self.baidu_url + self.keywords + '&pn=' + str(10*i)
            print(url)
            headers = self.get_new_headers()
            page = requests.get(url=url, headers=self.headers)
            time.sleep(random.uniform(1.1,5.4))
            # print(page.text)
            page.encoding = 'utf8'
            # print(page.text)
            print(page.status_code)
            soup = BeautifulSoup(page.text, "html5lib")
            tagh3 = soup.find_all('h3')
            for h3 in tagh3:
                print("HI")
                try:
                    href = h3.a.attrs['href']
                except:
                    href = None
                    print("读取百度页面失败")
                    continue
                print(href)
                result = self.get_info_request(href, headers)
                if result == None:
                    pass
                else:
                    print("result = ", result)
                    result["url"] = href
                    return_context.append(result)

        return return_context

            # try:
            #     href = h3.a.attrs['href']
            #     print(href)
            #     print(type(href))
            #     self.get_request(href)
            # except :
            #     time.sleep(10)
            #     print("Error")
            #     break


            # if real_url.startswith('http'):
            #     all.write(real_url + '\n')




# def main():
#     url = 'http://www.wuhanzhengtian.com/'
#     keswords = '在线无码av高清毛片'
#     keywordsspider= KeywordsSpider(keswords)
#     keywordsspider.get_urls_from_baidu()
#
# if __name__ == '__main__':
#     main()
