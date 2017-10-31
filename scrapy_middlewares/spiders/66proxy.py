#coding:utf8
import scrapy
from scrapy_middlewares.items import Proxy66Item

class Proxy66(scrapy.Spider):
    name = 'proxy66'
    allow_domain = ['66ip.cn']

    # 内置其实请求函数，生成所有请求对象
    def start_requests(self):
        base_url = 'http://www.66ip.cn/areaindex_35/%d.html'
        # 构造分页请求
        for i in range(1,10):
            fullurl = base_url % i
            yield scrapy.Request(fullurl,callback=self.parse)

    # 列表页面解析
    def parse(self, response):
        ip_list = response.xpath('//div[@align="center"]/table//tr')[1:]
        for host in ip_list:
            item = Proxy66Item()
            ip = host.xpath('.//td[1]/text()').extract()[0]
            port = host.xpath('.//td[2]/text()').extract()[0]

            item['ip'] = ip
            item['port'] = port

            print dict(item)


