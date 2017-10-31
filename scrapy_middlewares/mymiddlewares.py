#coding:utf8
from scrapy.conf import settings
import random
from selenium import webdriver
from scrapy.http import HtmlResponse

class RandomProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(settings['PROXIES'])
        print proxy
        if proxy.get('auth') is None:
            request.meta['proxy'] = 'http://' + ':'.join([proxy['ip'], proxy['port']])


class PhantomjsMiddleware(object):
    def __init__(self):
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
        )
        self.browser = webdriver.PhantomJS(desired_capabilities=dcap)

    def process_request(self,request,spider):
        if spider.name == 'baiduip':
            # 通过请求对象获取请求url
            self.browser.get(request.url)
            print 'phantom发起请求'
            return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source,encoding='utf-8',request=request)