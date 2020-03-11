USER_AGENTS = [
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

USER_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookies': '',
    'Host': 'www.biquge.com.cn',
    'Referer': '',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':''
}



MAIN_TAGET_URL = [
    '/xuanhuan/',
    '/xiuzhen/',
    '/dushi/',
    '/lishi/',
    '/wangyou/',
    '/kehuan/',
    '/yanqing/',
    '/qita/',
    '/quanben/'
]
MAIN_TAGET_TITLES = [
    '玄幻小说',
    '修真小说',
    '都市小说',
    '历史小说',
    '网游小说',
    '科幻小说',
    '言情小说',
    '其他小说',
    '完结小说'
]

DATABASE_NAME = 'books' # 数据库名字

BOOK_INFOS_COLLECTION = 'book_infos' # 存储书籍基本信息的表名（集合名）
BOOK_ID = 'book_id'
INFOS_CLASS = 'book_class'
INFOS_NAME = 'book_name'
INFOS_AUTHER = 'book_auther'
INFOS_IMG_URL = 'book_img_url'
INFOS_STATUS = 'book_status'
INFOS_LAST_UPDATE_TIME = 'book_last_updata_time'
INFOS_LAST_UPDATE_DESC = 'book_last_updata_desc'
INFOS_LAST_UPDATE_URL = 'book_last_updata_url'
INFOS_DECS = 'book_desc'

BOOK_DETAILS_COLLECTION = 'book_details'  # 存储书籍每一章信息的表名（集合名）
DETAILS_NEXT_URL = 'next_url'
DETAILS_CAPTER_NUMB = 'book_capter_numb'
DETAILS_CAPTER_NAME = 'book_capter_name'
DETAILS_CONTENT = 'book_content'


BOOK_IMG_DIR = './static/book_imgs' # 图片存放路径

PROXY_POOL_URL = 'http://43.248.9.169:5555/random'
