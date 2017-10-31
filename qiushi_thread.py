# coding:utf8
import requests
import threading
import Queue
from lxml import etree
import time
import random
import json

concurrent = 3
parse_count = 3


class CrawlThread(threading.Thread):
    def __init__(self, task_q, data_q, num, ):
        super(CrawlThread, self).__init__()
        self.task_q = task_q
        self.data_q = data_q
        self.num = num + 1
        self.sess = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        self.sess.headers = self.headers

    def run(self):
        print '启动面壁人%d号' % self.num
        while self.task_q.qsize() > 0:  # 队列长度大于0
            url = self.task_q.get()
            print '%d号机器人采集%s' % (self.num, url)

            time.sleep(random.randint(1, 3))
            response = self.sess.get(url)
            html = response.text
            self.data_q.put(html)
        print '结束机器人%d号' % self.num


# 解析线程
class ParseThread(threading.Thread):
    def __init__(self, data_q, crawl_list, num, lock, f):
        super(ParseThread, self).__init__()
        self.data_q = data_q
        self.crawl_list = crawl_list
        self.num = num + 1
        self.is_parse = True  # 是否解析
        self.lock = lock
        self.f = f

    def run(self):
        print '启动解析机器人%d号' % self.num
        while True:
            for crawl in self.crawl_list:
                if crawl.is_alive():
                    break
            else:
                if self.data_q.qsize() == 0:  # 数据队列为空，并且所有采集线程执行完毕
                    self.is_parse = False

            if self.is_parse:
                try:
                    html = self.data_q.get(timeout=3)
                    # html = etree.HTML(html)
                    # print html.xpath('//title')[0].text, type(html.xpath('//title')[0].text)
                    # self.f.write(html.xpath('//title')[0].text.encode('utf-8') + '\n')
                    self.parse(html)
                except Exception, e:
                    pass
            else:
                break
        print '结束解析机器人%d号' % self.num

    def parse(self, html):
        html = etree.HTML(html)
        duanzi_div = html.xpath('//div[@class="article block untagged mb15"]')
        print duanzi_div

        for duanzi in duanzi_div:
            item = {}
            item['nick'] = duanzi.xpath('.//h2')[0].text
            age = duanzi.xpath('.//div[@class="articleGender womenIcon"] | .//div[@class="articleGender manIcon"]')
            if age:
                item['age'] = age[0].text

            item['content'] = duanzi.xpath('.//div[@class="content"]/span[1]')[0].text
            item['image'] = duanzi.xpath('.//div[@class="thumb"]//img/@src')
            item['happy_num'] = duanzi.xpath('.//span[@class="stats-vote"]//i[@class="number"]')[0].text
            item['common_num'] = duanzi.xpath('.//span[@class="stats-comments"]//i[@class="number"]')[0].text
            print item
            with self.lock:
                self.f.write(json.dumps(item,ensure_ascii=False).encode('utf-8') + '\n')


def main():
    # 任务队列
    task_q = Queue.Queue()

    # 数据队列
    data_q = Queue.Queue()

    # 锁
    lock = threading.Lock()
    # 打开文件对象
    f = open('duanzi.json', 'w')

    # 生成10个任务追加到任务队列里
    for i in range(0, 21):
        url = 'https://www.qiushibaike.com/history/c23360f73a534d6cece52b56caba27f6/page/%d/' % i
        task_q.put(url)

    # 启动采集线程
    crawl_list = []
    for num in range(concurrent):
        t = CrawlThread(task_q, data_q, num)
        t.start()
        crawl_list.append(t)

    # 启动解析线程
    parse_list = []
    for num in range(parse_count):
        t = ParseThread(data_q, crawl_list, num, lock, f=f)
        t.start()
        parse_list.append(t)

    # 等待所有采集线程运行完毕
    for crawl in crawl_list:
        crawl.join()

    # 等待所有解析线程运行完毕
    for parse in parse_list:
        parse.join()

    f.close()


if __name__ == '__main__':
    start = time.time()
    main()
    print 'resume', time.time() - start
