## cookies session的区别
- cookies数据放在客户端浏览器上，session数据放在服务器上
- cookies不是很安全，分析cookies可以，伪造cookies
- session会在一定时间内保存在服务器上。访问增多，会影响服务器性能
- 单个cookies值不能超过4K。很多浏览器都限制一个站点最多保存20个cookie

## 爬虫带cookies和session的优缺点
- 优点： 能够访问到登录之后的页面
- 缺点： 一套cookies和session往往和一个用户对应
-- 请求太快，请求次数太多，容易被服务器识别为爬虫
- 结论： 不需要cookies的时候尽量不适用cookies
- 为了获取登录之后的页面，我们必须适用带上这两个东西

## 简单处理一下: requests的有一个session类，来实现回话保持

```python
session = requests.session()
# 实例化session
post_url = "一般是一个登录页面"
data_post = {
    "用户名": 用户名，
    "密码"：密码
}
response = session.post(url=post_url, data_post=data_post, headers=headers)
# 先使用session发送请求，登录对应的网站，把cookies保存在session中
get_url = "等之后才能访问的页面"
request = session.get(url=get_url, headers=headers)
# 再使用session请求登录之后才能访问的网站，session能够自动的携带登录成功时的cookies，进行请求
# 注意两次请求，一次用的是post，一次用的get
```

## 字典、列表推导式

```python
cookies = {}
cookies = [i.split("=")[0]:i.split("=")[1] for i in range(cookies.split("; "))]
```
