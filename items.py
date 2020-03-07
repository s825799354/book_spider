# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    cat = scrapy.Field()
    book_id = scrapy.Field()
    book_name = scrapy.Field()
    author_name = scrapy.Field()
    last_update_time = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    new_chapter = scrapy.Field()

class chapterItem(scrapy.Item):
    book_id = scrapy.Field()
    content = scrapy.Field()
    chapter_name = scrapy.Field()
    chapter_id = scrapy.Field()