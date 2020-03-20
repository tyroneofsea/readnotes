### requets post
### 应用场景：登录注册、大量数据提交等
- 发送post请求
- 使用代理
- 处理cookies、session

## 用法
```python
response = requests.post(url=url, data=data, headers=headers)
data:字典形式
```
## 好用的工具(文件以.json结尾)
- atom里面有一个叫pretty-json的插件，考虑一下，格式化json
- pycharm里面code=>Reformat Code。（如果在pycharm中中文无法显示，复制到ipython中查看，当然这个键可以格式化大多数文件：html、py，都可以格式化）

```python
import requests
import sys
import json


query_string = sys.argv[1]

headers = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
}
post_data = {
    "query": query_string,
    "from": "zh",
    "to": "en"
}

post_url = "http://fanyi.baidu.com/basetrans"
r = requests.post(url=post_url, data=post_data, headers=headers)
dict_ret = json.loads(r.content.decode())
ret = dict_ret["trans"][0]["dst"]
print("result is: ", ret)

## 使用方式python 你命名这个文件的名字 你要翻译的内容
```

## alias的使用

```python
vim /home/.bashrc
# 添加一行

alias fanyi="python 你写的上面python文件的绝对路径"
# 保存退出
source ~/.bashrc
# 这样就可以实现你输入： fanyi 你想要翻译的内容
# 回车即可运行上面的文档

```

## 代理

```python
proxies = {
    "http": "http://IP:PORT",
    "https": "https://IP:PORT"
}
requests.get(url=url, proxies=proxies)
```
