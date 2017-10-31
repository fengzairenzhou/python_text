# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import os

class TempSpider(scrapy.Spider):
    name = 'temp'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://sou.zhaopin.com/']

    def parse(self, response):
        a = 0
        # for i in response.xpath('//div[@id="newlist_list_content_table"]//div/a/@href').extract():
        #     if 'jobs.zhaopin.com' in i:
        #         print i
        #         a += 1
        #         print a
        # print os.path.dirname(__file__)

        # with open('type.html','r') as f:
        #     html = f.read()
        #     html = etree.HTML(html)
        #     city_list = html.xpath('//div[@class="paddingTB"]/table//input/@value')
        #     print city_list
