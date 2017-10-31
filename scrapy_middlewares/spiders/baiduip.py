# -*- coding: utf-8 -*-
import scrapy

class BaiduipSpider(scrapy.Spider):
    name = 'baiduip'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response):
        print response.body
