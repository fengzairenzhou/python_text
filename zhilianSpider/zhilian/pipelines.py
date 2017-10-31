# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime

class ZhilianPipeline(object):
    def process_item(self, item, spider):
        item['crawled'] = datetime.utcnow()  # 获取当前utc时间
        item['spider'] = spider.name  # 爬虫名称
        return item
