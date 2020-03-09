import urllib
import requests

PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
    try:
        res = requests.get(PROXY_POOL_URL)
        if res.status_code == 200:
            return res.text
    except ConnectionError:
        return None



def get_html(use_url):
    # use_url = self.url + url
    print("spidering url =========>",  use_url)
    req = urllib.request.urlopen(url=use_url)
    try:
        html = req.read().decode('utf-8')
        print("获取到html")
    except:
        print("没有获取到html")

    proxy = get_proxy()
    proxies = {
        'socket':  proxy,
        'socket5': proxy
    }

    proxy_support = urllib.request.ProxyHandler(proxies)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    try:
        a = urllib.request.urlopen(use_url).read().decode("utf8")
        print("获取到html")
    except:
        print("没有获取到html")

get_html('https://www.biquge.com.cn')
