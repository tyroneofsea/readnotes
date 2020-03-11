import urllib
import requests
from settings import *
import random



def get_proxy():
    try:
        res = requests.get(PROXY_POOL_URL)
        if res.status_code == 200:
            return res.text
    except ConnectionError:
        return None



def get_html(use_url):
    # use_url = self.url + url
    # print("spidering url =========>",  use_url)
    # req = urllib.request.urlopen(url=use_url)
    # try:
    #     html = req.read().decode('utf-8')
    #     print("获取到html")
    #     return html
    # except:
    #     print("没有获取到html")

    proxy = get_proxy()
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
        print("req = ", req)
        print("req.headers = ", req.headers)
        response = urllib.request.urlopen(req)
        print("response.headers = ", response.headers)
        html = response.read().decode("utf8")
        # print(html)
        print("获取到html")
        return html
    except:
        print("没有获取到html")
        return None

    # try:
    #     html = urllib.request.urlopen(use_url).read().decode("utf8")
    #     # print(html)
    #     print("获取到html")
    #     return html
    # except:
    #     print("没有获取到html")
    #     return None

get_html('https://www.biquge.com.cn')
