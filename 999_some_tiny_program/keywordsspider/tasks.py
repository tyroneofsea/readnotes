#tasks.py
from celery import Celery
from mongomanager import KeywordsMongo
import keywordsspider

app = Celery('tasks',  backend='redis://localhost:6379/0', broker='redis://localhost:6379/0') #配置好celery的backend和broker


@app.task  #普通函数装饰为 celery task
def long_task(keyname):
 # 耗时任务的逻辑
 print("start")
 kspider = keywordsspider.KeywordsSpider(keyname)
 return_context = kspider.get_urls_from_baidu()
 print("end")
 return result
