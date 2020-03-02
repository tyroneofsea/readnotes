# 万物一类
### python
你知道学习python或者说做一个高级打字员（程序猿）的前几步是什么吗？
下面是我认为的前几步：
- 你需要一个8G以上内存（最好16G）的电脑（条件不允许的情况下，强烈介入入手一个华为的电脑，去官网看一下哈，那么允许呢？答案是MAC）
- 购买一个8G以上的U盘
- （说一句，写这个人的真市侩：可略过）
- 用U盘安装一个ubuntu的电脑

windows很强大，很好。

在一定程度上讲，没有windons的话，也不需要有这么多人写这么多的代码。

但是windows并不适合一个要写程序的人。

做好上面的三步，然后我们继续

### 编辑器
- sublime text
- vs code
- atom
- pycharm

不存在高低之分：因为写代码的是你，而不是编辑器。

一般建议：新手用pycharm

写多了用：vs code或者atom

大神：什么是编辑器？vim足够完美了！


sublime text其实我用的体验并不好，但是！实在是太漂亮了！

哈哈哈

我猜你现在肯定在想，快告诉我们你最常用的编辑器就完事了。

是atom

当然notepad++，也很好用，写一个小东西的话，也可以考虑。


### 终于要出场了
```python
# 我比较菜
# 其实这个代码是从下往上写的：就是先有最下面的，然后有上面的
# 建议你也先看最下面的
import os


class OsTestClass(object):
    def __init__(self):
        pass

    def do_first_thing(self):
        pass

    def do_second_thing(self):
        pass

    def run(self):
        self.do_first_thing()
        self.do_second_thing()

    def __del__(self):
        pass


def main():
    ostest = OsTestClass()
    ostest.run()

if __name__ == '__main__':
    main()

```

### 什么？？？你已经看懂上面的代码了？！！
### 恭喜你，你已经会python了
- 先看这段，这段表示当程序执行到这里的时候，它会执行下面的函数也就是main()
```python
if __name__ == '__main__':
    main()
```
- 然后看下面这段，这里有几个要注意的地方
-- def:表示这是一个函数，函数名字叫main(),空的括号意味着他并不需要传入参数
```python
def main():
```
-- 下面这段看上去像是一个赋值，但是准确来说，它叫创建了一个类的对象(毕竟万物一类嘛，不是么？)
```python
ostest = OsTestClass()
```
-- 下面这段叫调用了这个类里面的一个方法，这个方法叫run()，不需要传入参数。那么这个方法在什么地方呢？去定义类的地方找。也就是上面。
```python
ostest.run()
```
-- 去找到下面的代码，看看ostestrun()要干嘛,哦，原来它要干第一件事，第二件事，这里有一个参数self哦，因为它是一个类方法
```python
def run(self):
    self.do_first_thing()
    self.do_second_thing()
```
-- 找到下面的代码，看看do_first_thing和do_second_thing干了什么:pass意味着它什么也没做
```python
def do_first_thing(self):
    pass
def do_second_thing(self):
    pass
```
-- 然后来看看这行代码:原来类定义在这里哦，注意这里有一个参数object，说明这个类继承自object。还记得万物一类么？这个object就是那个万物的爸爸~~！
```python
class OsTestClass(object):
```
-- 好像遗漏了什么？是的，"__init__"和"__del__"。__init__：会在实例化之前使用；__del__: 会在实例销毁之前使用。简单点init在实例化之前执行，如果init错误，实例化会终止，就是说类的对象会创建失败。del就是会在实例销毁之前用，如果del错误，那么销毁也会报错。
好难哦~~为什么会有这么奇奇怪怪的东西，相信我，你会爱上他们的。
相信我，难的还在后面。
```python
    def __init__(self):
        pass

    def __del__(self):
        pass
```
-- 好像还遗漏了什么？下面这个代码是导入一个东西：为什么叫它东西呢？因为它可能是一个库、一个方法、一个类。所以它只能是个东西了~~
```python
import os
```

### 如果你看懂了上面的东西，那么又一次恭喜你，你学会了python了。
什么！我会了？

是的，不信，我总结给你看

注意那些顶格写的东西：

- import: 导入一个东西，这会能让你用别人的东西
- class：这是一个类，能让你写自己的类，记得在括号里继承
- def：函数或者叫方法，能让写自己的方法，还可以带参数
- if __name__ == '__main__'：只能有一个入口函数，就是程序到这个地方开始执行

python再怎么写能跑得出这个范围吗？

或许可以，但是没有必要。哈哈哈

### 没错，你会了！
### 写点有用的吧，哈哈哈

```python
# 我比较菜
# 其实这个代码是从下往上写的：就是先有最下面的，然后有上面的
# 建议你也先看最下面的
import os


class OsTestClass(object):
    def __init__(self):
        pass

    def do_first_thing(self):
        print(os.getcwd())

    def do_second_thing(self):
        print(os.getcwdb())

    def run(self):
        self.do_first_thing()
        self.do_second_thing()

    def __del__(self):
        pass


def main():
    ostest = OsTestClass()
    ostest.run()

if __name__ == '__main__':
    main()

```

把上面的文字写入一个名字为：os_test.py的文件中,进入os_test.py所在的文件夹
```python
python3 os_test.py
```

注意一下两次输出的不同

至于__init__和__del__，在用python操作mysql的时候会用到，从那天开始，你会爱上他们的。

### 补充一下命名规则
- 函数或者叫方法用下划线连接，比如：do_first_thing()
- 类遵循驼峰规则，比如：OsTestClass()
- 变量 和方法一样，比如：do_first_thing_num
- 怎么区分是变量和方法呢？仔细看，仔细想，你会知道的
- 两格下划线开头的、保留字（比如def）不能用


有空多看PEP8：就是书写规范，命名规则PEP8里面都有，常用的有下面几个：
- import 和下面的代码空两格
- 类和类之间空两格
- 在一个类内部方法（就是类方法）：空一格


祝你好运





                                        2020.03.02半夜01:36 Alex Tyrone

                                        真是寂寞如雪啊~~~~~~~~~~~~~~~~~~~~~~~~
