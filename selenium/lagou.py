#coding:utf8
from selenium import webdriver
from lxml import etree
import time
from mysql_demo import Mydb
mydb = Mydb()

# 加 useragent
# ------------------------------------------------------------------------------------------------------------------
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
)
browser = webdriver.PhantomJS(desired_capabilities=dcap)
# ------------------------------------------------------------------------------------------------------------------

browser.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')

while True:
    #匹配所有职位div
    html = etree.HTML(browser.page_source)
    position_list = html.xpath('//div[@class="s_position_list "]/ul/li')
    # 遍历一个页面的所有职位
    for position in position_list:
        position_name = position.xpath('.//h3/text()')[0]
        print 'crawling...', position_name
        location = position.xpath('.//em/text()')[0]
        money = position.xpath('.//span[@class="money"]/text()')[0]
        company = position.xpath('.//div[@class="company_name"]/a/text()')[0]
        date_pub = position.xpath('.//span[@class="format-time"]/text()')[0]
        #组装sql语句
        sql = 'insert into lagou_position(position_name,location,money,company,date_pub) ' \
              'values("%s","%s","%s","%s","%s") on duplicate key update ' \
              'money=values(money),company=values(company),date_pub=values(date_pub)' % (position_name,location,money,company,date_pub)
        # 执行sql
        mydb.execute(sql)

    # 点击下一页
    if browser.page_source.find('pager_next pager_next_disabled') != -1:
        break

    browser.find_element_by_class_name('pager_next ').click()
    time.sleep(0.5)

    #exit()
#browser.save_screenshot('lagou.png')

mydb.close()
