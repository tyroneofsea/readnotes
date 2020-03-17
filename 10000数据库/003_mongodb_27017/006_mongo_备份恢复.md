### 备份语法（在终端中直接输入这些数据）
```python
mongodump -h dbhost -d dbname -o dbdirectory
# -h 指定服务器地址，也可以指定端口号(本地可以省略)
# -d 需要备份的数据库名称
# -o 备份数据存放位置，此目录中存放着备份出来的数据
# 例子
mongodump -h 98.56.211.34:27017 -d test1 -o ~/Desktop/test1bak
```

## 数据恢复语法

```python
mongorestore - dbhost -d dbname --dir dbdirectory
# -h 恢复数据的服务器地址(本地可以省略)
# -d 需要恢复的数据库实例
# --dir 备份数据所在的位置
# 例子
mongorestore -h 45.66.66.66:27017 -d test2 --dir ~/Desktop/test1bak/test1
```
