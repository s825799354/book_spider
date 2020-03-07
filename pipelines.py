# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
from book.items import BookItem, chapterItem


class BookPipeline(object):
    def open_spider(self, spider):
        self.con = pymysql.connect(host='localhost',
                                   user='root',
                                   password='root',
                                   db='book_spider',
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        with self.con.cursor() as cur:
            if (isinstance(item, chapterItem)):
                sql = "insert into `book_chapter`(`book_id`,`chapter_name`,`content`,`chapter_id`) values (%s, %s,%s,%s)"
                cur.execute(sql, (item['book_id'], item['chapter_name'], item['content'], item['chapter_id']))
            elif (isinstance(item, BookItem)):
                sql = "insert into `book_info`(`cat`,`book_id`,`book_name`,`last_update_time`,`author_name`,`create_time`,`update_time`,`new_chapter`) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(sql,(item['cat'],item['book_id'],item['book_name'],item['last_update_time'],item['author_name'],item['create_time'],item['update_time'],item['new_chapter']))
            self.con.commit()
        return item

    def close_spider(self, spider):
        self.con.close()
