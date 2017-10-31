# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor  # 专门提取页面链接
from scrapy.spiders import CrawlSpider, Rule  # 处理链接请求
import re

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php/']

    #  提取链接规则
    rules = (
        # follow : 是否跟进页面 根据规则 进行再次提取链接
        Rule(LinkExtractor(allow=(r'position_detail',)), callback='parse_item', follow=False,process_links='pro_link'),
        Rule(LinkExtractor(allow=(r'start=\d+',)), follow=True),
    )

    # 处理职位详情
    def parse_item(self, response):
        position_name = response.xpath('//tr[@class="h"]/td/text()').extract()[0]
        location = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
        position_type = response.xpath('//tr[@class="c bottomline"]/td[2]/text()').extract()[0]
        position_num = response.xpath('//tr[@class="c bottomline"]/td[3]').extract()[0]
        position_num = self.getNumber(position_num)
        print position_name,location,position_type,position_num

    # 处理链接
    def pro_link(self,links):
        for link in links:
            link.url = link.url.replace('position.php/', '')
        return links

    def getNumber(self, data):
        num_re = re.compile(r'\d+')
        res = num_re.search(data)
        if res is not None:
            return int(res.group())
        else:
            return 0