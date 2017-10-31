# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from scrapy.pipelines.images import ImagesPipeline
import json
import hashlib
# 异步数据库操作api
from twisted.enterprise import adbapi
import MySQLdb.cursors


def getMd5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()



class Py02ScrapyDay11Pipeline(object):
    def process_item(self, item, spider):
        return item


# 写入json
class CnBlogJsonPipeline(object):
    def __init__(self):
        self.f = open('cnblog.json', 'w')

    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), ensure_ascii=False).encode('utf-8') + '\n')
        # 返回数据对象,交给其它的管道文件进行处理
        return item

    def close_spider(self, spider):
        self.f.close()


# 保存图片的Pipeline
class CnblogImagePipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     pass
    def item_completed(self, results, item, info):
        # 图片处理结果
        status = results[0][0]
        if status:
            item['image_path'] = results[0][1]['path']
        else:
            item['image_path'] = ''

        return item


# 同步写入mysql
class CnblogMysqlPipeline(object):
    # 初始化
    def __init__(self):
        try:
            self.conn = MySQLdb.connect('127.0.0.1', 'root', '123', 'temp', charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception, e:
            print '数据库连接失败'
            print str(e)

    def process_item(self, item, spider):
        print dict(item)
        sql = 'insert into cnblogs(title,content,url,image_path,article_desc,author,date_pub,article_view,article_common) ' \
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update title=values(title),content=values(content),image_path=values(image_path),article_desc=values(article_desc),' \
              'author=values(author),article_view=values(article_view),article_common=values(article_common)'

        # print sql
        try:
            self.cursor.execute(sql, (item['title'],item['content'],getMd5(item['url']),item['image_path'],item['article_desc'],item['author'],item['date_pub'],item['article_view'],item['article_common'],))
            self.conn.commit()
        except Exception, e:
            print '插入失败',str(e)
        return item

    # 最后调用
    def close_spider(self):
        self.cursor.close()
        self.conn.close()


# 异步写入mysql pipeline
class TwistedCnblogMysqlPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    # 方法名是固定的
    @classmethod # 类方法 静态方法 先加载类静态方法，优先__init__执行
    def from_settings(cls, settings):
        db_config = dict(
            host = settings['MYHOST'],
            user = settings['MYUSER'],
            passwd = settings['MYPASSWORD'],
            db = settings['MYDB'],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
        )
        # 数据库连接池
        dbpool = adbapi.ConnectionPool('MySQLdb' ,**db_config)
        return cls(dbpool)

    def process_item(self,item,spider):
        # 异步插入操作
        query = self.dbpool.runInteraction(self.insert,item)
        query.addErrback(self.handle_error)
        return item

    # 插入操作
    def insert(self,cursor,item):
        sql = 'insert intoo cnblogs(title,content,url,image_path,article_desc,author,date_pub,article_view,article_common) ' \
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update title=values(title),content=values(content),image_path=values(image_path),article_desc=values(article_desc),' \
              'author=values(author),article_view=values(article_view),article_common=values(article_common)'
        cursor.execute(sql,(item['title'],item['content'],getMd5(item['url']),item['image_path'],item['article_desc'],item['author'],item['date_pub'],item['article_view'],item['article_common'],))

    #错误处理函数
    def handle_error(self,error):
        print str(error)