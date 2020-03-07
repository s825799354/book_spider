# code=utf-8
import scrapy
from book.items import chapterItem, BookItem
import time


class BookSpider(scrapy.spiders.Spider):
    name = 'book_spider'
    dont_redirect = True
    handle_httpstatus_list = [301,302]
    # request.meta['handle_httpstatus_list'] = [301,302]

    def start_requests(self):
        print(22222222222222222)
        url = 'http://www.xbiquge.la/xiaoshuodaquan/'
        yield scrapy.Request(url=url, callback=self.parse_lists, dont_filter=True)

    def parse_lists(self, response):
        if response.status == 302:
            yield scrapy.Request(url=response.url, callback=self.parse_lists, dont_filter=True)
            return

        # todo 获取待爬取的url组成的列表
        urls = response.css('div.novellist ul li a::attr(href)')
        for url in urls:
            url = url.get()
            yield scrapy.Request(url=url, callback=self.parse_book, dont_filter=True)

    def parse_book(self, response):
        if response.status == 302:
            yield scrapy.Request(url=response.url, callback=self.parse_book, dont_filter=True)
            return

        try:
            # 小说章节列表
            lists = response.css('#list dl dd')
            book_item = BookItem()
            book_id = response.url.split('/')[-2]
            book_item['cat'] = response.css('#wrapper > div:nth-child(5) > div.con_top > a:nth-child(3)::text').get()
            book_item['book_id'] = book_id
            book_item['book_name'] = response.css("#info > h1::text").get()
            book_item['author_name'] = response.css("#info > p:nth-child(2)::text").get().split('：')[-1]
            book_item['last_update_time'] = response.css('#info > p:nth-child(4)::text').get().split("：")[-1]
            book_item['last_update_time'] = '%d' % time.mktime(
                time.strptime(book_item['last_update_time'], '%Y-%m-%d %H:%M:%S'))
            book_item['new_chapter'] = response.css('#info > p:nth-child(5) > a::text').get()
            book_item['create_time'] = '%d' % time.time()
            book_item['update_time'] = '%d' % time.time()
            yield book_item
            for l in lists:
                url = l.css('a::attr(href)').get()
                # print(url)
                yield scrapy.Request(url='http://www.xbiquge.la' + url, callback=self.parse_chapter,
                                     meta={'book_id': book_id}, dont_filter=True)
        except IndexError:
            print('索引错误')

    def parse_chapter(self, response):
        if response.status == 302:
            yield scrapy.Request(url=response.url, callback=self.parse_chapter, dont_filter=True, meta=response.meta)
            return
            # todo
        book_id = response.meta['book_id']
        chapter_name = response.css('#wrapper > div.content_read > div > div.bookname > h1::text').get()
        res = response.xpath('//*[@id="content"]/text()').getall()
        # 合并文本节点
        res = ''.join(res)
        # 去掉\xa0符号
        content = ''.join(res.split())

        item = chapterItem()
        item['book_id'] = book_id
        item['chapter_name'] = chapter_name
        item['content'] = content
        item['chapter_id'] = response.url.split('/')[-1][:-5]
        yield item
