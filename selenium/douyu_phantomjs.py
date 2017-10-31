# coding:utf8
from selenium import webdriver
from lxml import etree
import time
import json

browser = webdriver.PhantomJS()
browser.get('https://www.douyu.com/directory/all')
time.sleep(0.5)
# 直到不能点击下一页跳出循环
with open('douyu.json', 'w') as f:
    while True:
        html = browser.page_source
        html = etree.HTML(html)  # 解析html
        # title = html.xpath('//title/text()')[0]  #获取title
        # 获取整个房间li
        room_list = html.xpath('//div[@class="content allList-cont"]//ul[@class]/li')
        for room in room_list:
            # 房间名
            room_name = room.xpath('.//h3/text()')[0]
            # 房间直播人
            room_user = room.xpath('.//p/span[1]/text()')[0]
            # 房间观众
            room_gz_num = room.xpath('.//p/span[2]/text()')
            if room_gz_num:
                room_gz_num = room_gz_num[0]

            item = {}
            item['room_name'] = room_name.strip()
            item['room_user'] = room_user.strip()
            item['room_gz_num'] = room_gz_num

            f.write(json.dumps(item, ensure_ascii=False).encode('utf-8') + '\n')
            print 'wrting room %s' % room_name

        # 判断下一页不可点击则跳出循环
        next = 'shark-pager-disable-next'
        is_next = browser.page_source.find(next)
        if is_next != -1:
            break

        browser.find_element_by_class_name('shark-pager-next').click()
        time.sleep(0.5)
