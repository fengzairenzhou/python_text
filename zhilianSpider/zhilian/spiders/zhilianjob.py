# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import os
from zhilian.items import ZhilianItem
from scrapy_redis.spiders import RedisSpider

class ZhilianjobSpider(RedisSpider):
    name = 'zhilianjob'
    allowed_domains = ['zhaopin.com']
    redis_key = 'zhilianjob:start_urls'
    # start_urls = ['http://sou.zhaopin.com/']

    # 为了启动分布式爬虫而准备
    def parse(self,response):
        print '1'*150
        start_url = 'http://sou.zhaopin.com/'
        yield scrapy.Request(url=start_url,callback=self.parse_start)

    # 获取工作类别
    def parse_start(self, response):
        print '2' * 150
        # 获取行业类别链接
        with open(os.path.join(os.path.dirname(__file__) + '\\type.html'), 'r') as f:
            html = etree.HTML(f.read())
            type_list = html.xpath('//div[@class="paddingTB"]/table//input/@value')
            # print type_list

        # 获取工作地点链接
        with open(os.path.join(os.path.dirname(__file__) + '/city.html'), 'r') as f:
            html = f.read()
            html = etree.HTML(html)
            city_list = html.xpath('//div[@class="sPopupTabCB"]/table//input/@value')
            # print city_list

        for each in response.xpath('//div[@id="search_bottom_content_demo"]/div[@class="clearfixed"]/h1'):
            # 获取职位类别名
            # position_list = each.xpath('./a/text()').extract()
            # for job in position_list:
            #     print job

            # 获取职位链接
            position_url = each.xpath('./a/@href').extract()
            for url in position_url:
                for types in type_list:
                    for city in city_list:
                        job_url = 'http://sou.zhaopin.com/'+url+'&in='+types+'&jl='+city

                        yield scrapy.Request(job_url,callback=self.parse_list)

    # 获取工作列表
    def parse_list(self,response):
        print '3' * 150
        for i in response.xpath('//div[@id="newlist_list_content_table"]//div/a/@href').extract():
            if 'jobs.zhaopin.com' in i:
                yield scrapy.Request(url=i,callback=self.parse_detail)
        next_page = response.xpath('//a[@class="next-page"]/@href').extract()
        if next_page:
            yield scrapy.Request(next_page[0],callback=self.parse_list)

    # 提取所需数据
    def parse_detail(self,response):
        print '4' * 150
        item = ZhilianItem()
        # f = lambda x: x[0] if x else ''
        item['detail_url'] = response.url
        item['pos_name'] = response.xpath('//div[@class="top-fixed-box"]//h1/text()').extract()[0]
        item['salary'] = response.xpath('//div[@class="terminalpage-left"]/ul/li/strong/text()').extract()[0]
        item['pub_date'] = response.xpath('//div[@class="terminalpage-left"]/ul/li/strong/span/text()').extract()[0]
        item['edu_bg'] = response.xpath('//div[@class="terminalpage-left"]/ul/li/strong/text()').extract()[3]
        item['experience'] = response.xpath('//div[@class="terminalpage-left"]/ul/li/strong/text()').extract()[2]
        item['location'] = response.xpath('//div[@class="terminalpage-left"]//h2/text()').extract()[0].strip()
        item['company'] = response.xpath('//div[@class="top-fixed-box"]//h2/a/text()').extract()[0]
        # item['pos_desc'] = f(response.xpath('//div[@class="terminalpage-left"]//div[@class="tab-inner-cont"]'
        #                                   '/p//span[@style]/text()|//div[@class="terminalpage-left"]'
        #                                   '//div[@style]/text()').extract())
        item['pos_desc'] = response.xpath('//div[@class="terminalpage-main clearfix"]').extract()
        # print item
        yield item
