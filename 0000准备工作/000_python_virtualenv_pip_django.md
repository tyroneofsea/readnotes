### python
ubuntu 自带python,且ubuntu20开始不自带python2
```python
python --version
或者
python3 --version
pip3 --version
# 如果没有输出pip3的版本信息
sudo apt-get install python3-pip
sudo pip3 --upgrade pip
# 更新到最新的pip
# pip是一个python包的管理工具
# 如果想了解更多pip或者pip到底管理着哪些包
# 访问：pipy.org
# 如果你访问不了，我也很无奈啊
```
### virtualenv:虚拟环境
```python
virtualenv --version
# 如果没有正常输入virtualenv的版本信息
pip3 install virtualenv
virtualenv -p python3 yourVirtualenvName
virtualenv -p python3 myDjangoLenv
# 这个命令会在你当前所在的文件夹下创建一个名为
# myDjangoLenv的文件夹，这个就是你的django的虚拟环境
# 多一句嘴：
为每一个项目分配一个属于他自己的虚拟环境是一个良好的习惯
希望你能遵守！
source myDjangoLenv/bin/activate
# 进入虚拟环境
deactivate
# 离开虚拟环境
注：如果没有特殊说明，往后的每个安装（pip）都是在虚拟环境中输入命令的！
```
### pip 和 virtualenv
```python
source myDjangoLenv/bin/activate
# 进入虚拟环境
pip list
pip freeze
# 显示当前虚拟环境中安装的包
pip freeze > requirements.txt
# 会在当前目录下生成一个requirements.txt文件，你打开看一下
# 这个命令会导出当前的包到一个requirements.txt文件中
# 这有什么用呢？
pip install -r requirements.txt
# 装 requirements.txt 中的所有包
# 知道导出这个文件requirements.txt有什么用了吗？
# 给别人拿到这个项目或者你自己要换一个电脑的时候，
# 可以以快速安装这个项目依赖的包
# 以后你会一直用到的
```
### Django
```python
# 提醒一下，进入虚拟环境
pip install django==2.1.7
# 安装django的2.1.7版本，为什么选择这个版本？
# 因为我喜欢这个数字~~（开玩笑的）
# 但是你要知道当你需要特定版本的时候应该怎么做了
django-admin --version
# 输出版本号
django-admin --help
# 如果一切顺利的话，你会看到一大堆英文
# 仔细看一下 “第一行”！！！！！
# 然后你就会知道下面这行为什么是这么写的
django-admin help startproject
# 稍微看一下，再坚持看一下，越前面的越重要
django-admin help startapp
# 再坚持一下，记住！越前面的越重要！
```

### 让我们开始吧
```python
# 记得进入虚拟环境
django-admin startprject myDjangoProgram
# 这个命令会让你在当前文件夹下创建一个名为myDjangoProgram的项目
cd myDjangoProgram
# 进入这个目录
ls
# 看一下这个目录
tree
# 看一下整个目录下的情况
```
