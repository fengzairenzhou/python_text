#coding:utf8
import urllib,urllib2
import re
import os

def getBaseUrl(tieba_name):
    '''
    :param tieba_name: 用户输入的贴吧名称
    :return: 贴吧的跟路由
    '''
    base_url = 'https://tieba.baidu.com/f?'
    qs = {
        'kw' : tieba_name
    }
    qs = urllib.urlencode(qs)
    base_url += qs

    # 根据tiebaname建立贴吧文件夹
    path = './images/' + tieba_name

    if not os.path.exists(path.decode('utf8')): #文件夹不存在 自动创建文件夹
        os.makedirs(path.decode('utf8'))

    return base_url


def getImage(href):
    '''
    :param href: 帖子详情链接
    :return:
    '''
    response = urllib2.urlopen(href)
    html = response.read()
    image_pattern = re.compile('class="BDE_Image".*?src="(.*?)"')
    # 获取所有图片地址
    image_url_list = image_pattern.findall(html)
    for image_url in image_url_list:

        # 获取图片名称
        file_name = image_url.split('/')[-1]

        fullname = os.path.join(u'./images/' ,tieba_name.decode('utf8'),file_name.decode('utf8'))

        # print type(tieba_name),type(fullname)
        print 'downloading...' + fullname
        urllib.urlretrieve(image_url,fullname)
        pass


def getTieBaPage(base_url):
    '''
    :param base_url: 贴吧根路由
    :return:
    '''
    response = urllib2.urlopen(base_url)
    html = response.read()

    #正则获取最大页数
    # re.S  能够让 . 匹配多行模式
    last_page_pattern = re.compile(r'next pagination-item.*?<a.*?href=".*?pn=(\d+)"',re.S)
    res = last_page_pattern.search(html)
    if res is not None:
        last_page = res.group(1)
        last_page = int(last_page)
    else:
        last_page = 10

    # 循环page
    start = 1
    end = last_page / 50  + 1
    page_start = raw_input('请输入开始页数--范围：%d-%d' % (start,end))
    page_end = raw_input('请输入结束页数--范围：%d-%d' % (start,end))


    tieba_url = 'https://tieba.baidu.com'

    for page in range(int(page_start), int(page_end) + 1 ):
        # 假设一共3页  pn  0  50 100
        # page             1  2  3
        pn = (page - 1) * 50
        fullurl = base_url + '&pn=' + str(pn)
        response = urllib2.urlopen(fullurl)
        page_html = response.read() # 某一页的html

        # 提取a 的href 链接正则
        href_pattern = re.compile(r'<a.*?href="(/p/.*?)"')
        href_list = href_pattern.findall(page_html)
        for href in href_list:
            # 每个帖子的链接地址
            getImage(tieba_url + href)



if __name__ == '__main__':
    tieba_name = raw_input('贴吧名称：')

    base_url = getBaseUrl(tieba_name)
    getTieBaPage(base_url)

