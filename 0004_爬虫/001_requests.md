## requests
### 安装
```python
# 进入虚拟环境
pip install requests
```
### 先了解一下
```python
response = requests.get(url=url, headers=headers, proxies=proxies)
# url 不解释了吧
# headers 如果不知道你需要多了解一下基础知识了哦
# proxies 代理，后面会用
# 还有一些其他参数，比如timeout什么的
# 这里面除了url之外，都可以为空
response.text
response.context
response.status_code
response.request.headers
response.headers
# 常用的方法
```

### 随手写几个例子
```python
import requests


res = requests.get("http://www.bing.com")
print(res.status_code)
assert res.status_code == 200
assert res.status_code == 300
print(res.headers)
res.request
```
