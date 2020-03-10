import requests


class Tieba(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = 'https://tieba.baidu.com/f?kw='+ tieba_name + '&ie=utf-8&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        }

    def get_url_list(self):  # 1 获取要访问的url list
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i*50) for i in range(1000)]
        # 扁平胜于嵌套

    def parse_url(self, url):
        response = requests.get(url=url, headers=self.headers)
        return response.content.decode()
        # 默认使用utf8

    def save_html(self, html_str, page_num):  # 保存html字符串
        file_path = "{}--第{}页".format(self.tieba_name, page_num)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(html_str)



    def run(self): # 实现主要逻辑
        # 1 获取要访问的url list
        url_list = self.get_url_list()

        for url in url_list:
            # 2 遍历url list 获取响应
            page_num = url_list.index(url) + 1
            html_str = self.parse_url(url)
            # 3 保存
            self.save_html(html_str, page_num)


def main():
    tieba = Tieba("李毅")


if __name__ == '__main__':
    main()
