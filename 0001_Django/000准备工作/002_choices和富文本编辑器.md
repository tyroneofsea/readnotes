### choices 和 富文本编辑器
### tinymce安装
```python
pip install tinymec==2.6.0
# 安装tinymce
# 当然富文本编辑器有很多种，你可以选择使用
pip list
# 查看一下是否安装在虚拟环境中
```
### 在settings.py中设置
```python
INSTALLED_APP = (
    ...
    ...
    'tinymce',
)
```

### 添加配置项：在settings.py中
```python
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'width': 600,
    'height': 400,
}
# 不要记住，去官网抄，复制黏贴即可
```
### 在settings.py同级目录下的urls.py中写入
```python
urlpatterns = [
    ...
    ...
    path('tinymce', include('tinymce.urls')),
]
```

### 使用tinymce
```python
# 理论上，可以在你想要的任何地方使用，但是一般在models类中使用
from tinymce.models import HTMLField
# 上面这行需要你写入
from django.db import models


```
