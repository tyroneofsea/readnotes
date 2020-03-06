## request带上headers（很多时候这个才是有用的）

### 先来看一下headers长得什么样子
```python

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

```
## 这里面有两个东西需要注意

第一：User-Agent，告诉服务器你用的是什么系统什么浏览器

第二：cookies,服务器告诉给你在本地设置的cookies
## 想一下这两个参数应该怎么解决
```python
# 第一个问题很容易解决，随便挑吧
# 怎么挑还记得么？
# import random
# USER_AGENTS[random.randint(0,20)]
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
# 第二个问题，应该怎么解决呢？分两种情况
# 第一种，这个网站不需要登录，那么他给你本地设置的cookies中大概率会有时间限制
# 就是说在一段时间以后，这个cookies会失效，怎么办呢？
url = '你的目标网站'
headers = {
    '你想要的headers'
}
res = requests.Session().get(url=url, headers=headers)
print(res.cookies)
# 每次你获取不到你想要的信息的时候，尝试换一下新的cookies


# 第一种问题（不需要登录的情况下，你可以用这种方式获得一个新的cookies）
# 第二种问题（需要登录）
# 比较复杂，简单来说：
# 第一步：模拟登录（大概率要遇到验证码，需要处理）
# 第二步：获得cookies（想一下上面的代码）
# 第三步：检测cookies是否失效，如果失效，返回第一步
# 当然如果你实现了这三步，那么我给你一个建议，不要只有一个账户，做一个cookie池吧
# 一个账号也是检测，多个账号也是检测，又不用你检测，为什么不多来几个呢？
```
