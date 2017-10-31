# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Py02ScrapyDay11Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CnblogItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field() # 图片链接
    image_path = scrapy.Field() # 图片路径
    article_desc = scrapy.Field()
    author = scrapy.Field()
    date_pub = scrapy.Field()
    article_common = scrapy.Field()
    article_view = scrapy.Field()
