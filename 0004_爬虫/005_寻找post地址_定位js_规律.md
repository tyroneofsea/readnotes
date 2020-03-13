### 寻找登录的post地址
- 在form表单中寻找action对应的url地址
 - post的数据是input标签中name的值作为键，真正的用户名密码作为值的字典，post的url地址就是action对应的url地址

 - 抓包（chrome F12） 寻找登录的url地址
    - 勾选perserve log按钮，防止页面跳转找不到url
    - 寻找post数据，确定参数（在最下面）（多试几次，用错误的密码）
        - 参数不会变，直接用，比如密码不是动态加密的时候
        - 参数会变：
            - 参数在当前的响应中。比如csrf_token
            - 通过js生成（看下面）

## 定位想要的js

- 选择会触发js事件的按钮，点击event listener，找到js的位置
- 通过chrome中的search all file 来搜索url中的关键词
- 添加断点的方式来查看js的操作，通过python来进行同样的操作
