#coding:utf8
import json
import redis
import MySQLdb

def main():
    # 指定redis数据库信息
    try:
        rediscli = redis.StrictRedis(host='192.168.2.129', port=6379, db=2,password='123456')
        # 指定mysql数据库
        mysqlcli = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123', db = 'temp', port=3306, charset='utf8')
    except Exception,e:
        print '数据库连接失败'
        print str(e)
        exit()

    while True:
        source, data = rediscli.blpop(["zhilianjob:items"])
        # print source # redis里的键
        # print data # 返回的数据
        item = json.loads(data)

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            sql = "insert into zhilian(spider,detail_url, pos_name,salary,pub_date,edu_bg,experience,location,company,pos_desc,crawled)" \
                  "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') on duplicate key update " \
                  "spider=values(spider),pos_name=values(pos_name),salary=values(salary),pub_date=values(pub_date),edu_bg=values(edu_bg)," \
                  "experience=values(experience),location=values(location),company=values(company),pos_desc=values(pos_desc),crawled=values(crawled)," \
                  % (item['spider'],item['detail_url'],item['pos_name'],item['salary'],item['pub_date'],item['edu_bg'],
                     item['experience'], item['location'], item['company'], item['pos_desc'],item['crawled'])

            cur.execute(sql)
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print "inserted %s" % item['spider']
        except Exception,e:
            print '插入失败'
            print str(e)

if __name__ == '__main__':
    main()