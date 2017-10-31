# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    detail_url = scrapy.Field() # 职位详情链接
    pos_name = scrapy.Field()   # 职位名称
    salary = scrapy.Field()     # 工资
    pub_date = scrapy.Field()   # 发布日期
    edu_bg = scrapy.Field()     # 教育背景
    experience = scrapy.Field() # 工作经验
    location = scrapy.Field()   # 工作地点
    company = scrapy.Field()    # 公司名称
    pos_desc = scrapy.Field()   # 职位描述

    crawled = scrapy.Field()    # 爬取时间
    spider = scrapy.Field()     # 爬虫名称
