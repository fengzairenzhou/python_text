#coding:utf8
import MySQLdb  # 引入mysql操作模块

# 数据库操作类
class Mydb:
    def __init__(self):
        try:
            self.conn = MySQLdb.connect('127.0.0.1','root','123','spider',charset='utf8') # 返回连接对象
            # 创建数据库操作游标
            self.cursor = self.conn.cursor()
        except Exception,e:
            print str(e)
            exit()

    # 查询操作
    def query(self,sql):
        try:
            self.cursor.execute(sql)
            # 拿到所有查询记录
            res = self.cursor.fetchall()
            return res
        except Exception,e:
            print str(e)

    # 执行增删改操作，需要commit
    def execute(self,sql):
        try:
            # 执行语句
            res = self.cursor.execute(sql)
            # 提交 innodb 引擎（事务）
            self.conn.commit()
            return res
        except Exception,e:
            print str(e)

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    mydb = Mydb()
    # sql = 'select * from user'
    # res = mydb.query(sql)
    # for user in res:
    #     print user[0],user[1]

    # 增加
    # sql = 'insert into user(`name`) values("%s")' % ('小美')
    # print sql

    # 更新
    # sql = 'update user set `name`="小妹儿",age=6 where id=2'

    # 删除操作
    sql = 'delete from user where id=1'
    mydb.execute(sql)
