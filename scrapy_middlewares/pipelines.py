# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class Py02SpiderDay14Pipeline(object):
    def process_item(self, item, spider):
        return item

class Mongo66Pipeline(object):
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(settings['MONHOST'],settings['MONPORT'])
    def process_item(self, item,spider):
        mongodb = self.mongo_client[settings['MONDB']]
        mongodb.host.insert(dict(item))
        # 必须要写
        return item