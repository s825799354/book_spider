# 顶点小说网全站爬取爬虫
#### 需要安装scrapy扩展和 pymysql扩展
#### 需要新建数据库 book_spider 然后导入sql文件
#### 命令行下执行爬虫
#### 如果想实现暂停功能 请参照[https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/jobs.html](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/jobs.html)
```
  python -m scrapy crawl book_spider
