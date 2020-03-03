## Gunicorn 和 Nginx 部署 Flask

### 结构
一个nginx ====》  若干个 Gunicorn上运行的flask  ===》数据库（mysql、redis，可能是集群）


### gunicorn安装以及使用
```python
pip install gunicorn
# 安装
gunicorn -h
# 查看帮助文档
gunicorn -w 4 -b IP:PORT -D --access-logfile ../../log ../../main:app
# -w : worker：表明进程数目
# -b : bind: 绑定IP和端口号（当然你运行在哪个机器上，就是哪个IP）
# -D 表明作为守护进程运行在后台
# --access-logfile ：指定日志文件保存位置（绝对路径）
# ../../main:app ：指定入口函数位置（绝对路径）
# 例：
gunicorn -w 4 -b 222.222.222.222:5000 -D --access-logfile /home/www/YourProgram/log  /home/www/YourProgram/main:app
# 这个下面会用到
```

### Nginx
```python
ps aux | grep nginx
# 如果你的服务器中已经存在nginx在运行，
# 那么这条命令会让你看到正在运行的nginx的配置文件的路径
# 找到他，然后用下面的命令复制他（免得你改错了）
sudo cp ../../nginx.conf  ../../nginx.conf.backup
sudo vim ../../nginx.conf
# 开始编辑nginx配置
# 在http{}中的server{}中添加如下内容
location / {
    proxy_pass http://flask;
    # proxy_pass 转发，转发到哪里
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    # 下面这两行的意思是告诉flask或者gunicorn用的IP和路由，不然flask永远获取到的IP信息都是nginx的IP
}
正确内容如下：有些内容来自上面
location / {
    proxy_pass http://222.222.222.222:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

### Nginx负载均衡（真实的部署，可能会比上面那个更加真实一点）
```python

http {
    ...
    upstream flasks {
        server 222.222.222.222:5555;
        server 222.222.222.222:6666;
        server 222.222.222.111:7777;
        server 222.222.222.222:7777;
    }
    # flasks 可以是任意名字
    # 仔细看上面的端口号和地址，你会发现一些东西哦
    # 如果你发现了，你就知道什么是负载均衡了
    ...
    server{
        listen  PORT(通常为80);
        servername IP or url;
        ...
        location / {
            proxy_pass http://flasks;
            # 注意这里的flasks，要和上面的upstream后面的名字一样了
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            # 下面这两行的意思是告诉flask或者gunicorn用的IP和路由，不然flask永远获取到的IP信息都是nginx的IP
        }
        ...
    }
    ...

}
```
