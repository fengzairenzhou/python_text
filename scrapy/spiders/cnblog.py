# -*- coding: utf-8 -*-
import scrapy
import re
from py02_scrapy_day11.items import CnblogItem


class CnblogSpider(scrapy.Spider):
    name = 'cnblog'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/']
    base_url = 'https://www.cnblogs.com'
    is_page = True  # 是否生成分页请求
    page = 1

    # 解析起始url的响应  解析列表页
    def parse(self, response):
        # 获取所有文章div
        article_list = response.xpath('//div[@class="post_item"]')
        for article in article_list:
            title = article.xpath('.//a[@class="titlelnk"]/text()').extract()[0]
            url = article.xpath('.//a[@class="titlelnk"]/@href').extract()[0]
            # 文章图片
            image_url = article.xpath('.//p[@class="post_item_summary"]/a/img/@src').extract()
            image_url = 'https:' + self.getValue(image_url)
            print image_url
            # 文章简介
            desc = article.xpath('.//p[@class="post_item_summary"]/text()[2]').extract()
            desc = self.getValue(desc)
            desc = self.format(desc)
            if desc == '':
                desc = article.xpath('.//p[@class="post_item_summary"]/text()[1]').extract()[0]

            # 文章作者
            author = article.xpath('.//div[@class="post_item_foot"]/a/text()').extract()[0]
            # 发布日期
            date_pub = article.xpath('.//div[@class="post_item_foot"]/text()[2]').extract()[0]
            date_pub = self.format(date_pub).split()[1]
            # 文章浏览数
            article_view = article.xpath('.//span[@class="article_view"]/a/text()').extract()[0]
            article_view = self.getNumber(article_view)
            # 文章评论
            article_common = article.xpath('.//span[@class="article_comment"]/a/text()').extract()[0]
            article_common = self.getNumber(article_common)

            info = {
                'title': title,
                'url': url,
                'image_url': image_url,
                'desc': desc,
                'author': author,
                'date_pub': date_pub,
                'article_view': article_view,
                'article_common': article_common,
            }
            # 构造请求，放入请求队列
            yield scrapy.Request(url=url, callback=self.parse_article, meta=info)

            # print author,date_pub,article_view,article_common
            # print '-' * 300
            # print title
            # print '-' * 300
            # print desc

        # 生成下一页请求
        # if self.page < 3:
        #     self.page += 1
        #     yield scrapy.Request(self.base_url + '/sitehome/p/%d' % self.page ,callback=self.parse)

        # next_page_url = response.xpath('//div[@class="pager"]/a/@href').extract()[-1]
        # yield scrapy.Request(url=self.base_url + next_page_url, callback=self.parse)

        # 生成所有分页请求，只生成一次
        if self.is_page:
            for i in range(2,4):
                fullurl = self.base_url + '/sitehome/p/%d' % i
                yield scrapy.Request(fullurl,callback=self.parse)
            self.is_page = False

    # 解析文章详情
    def parse_article(self, response):
        # 文章主要内容
        item = CnblogItem()

        title = response.meta['title']
        url = response.meta['url']
        desc = response.meta['desc']
        image_url = response.meta['image_url']
        author = response.meta['author']
        date_pub = response.meta['date_pub']
        article_view = response.meta['article_view']
        article_common = response.meta['article_common']
        content = response.xpath('//div[@id="post_detail"]').extract()[0]

        item['title'] = title
        item['url'] = url
        item['article_desc'] = desc
        item['image_url'] = [image_url]
        item['author'] = author
        item['date_pub'] = date_pub
        item['article_view'] = article_view
        item['article_common'] = article_common
        item['content'] = content

        # 交给itempipeline  管道文件
        yield item

    # 没有匹配到结果 则返回空
    def getValue(self, data):
        return data[0] if data else ''

    # 格式化字符串
    def format(self, data):
        return data.strip().replace('\n', '')

    def getNumber(self, data):
        num_re = re.compile(r'\d+')
        res = num_re.search(data)
        if res is not None:
            return int(res.group())
        else:
            return 0
