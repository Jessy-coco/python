"""
python
mysql数据库写操作
insert delete update
"""
import time
import pymysql
#连接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123123',
                   database='stu',
                   charset='utf8')
#获取游标（操作数据库，执行sql语句
cur=db.cursor()
# print(time.strftime("%Y-%m-%d"))
#写数据库
try:
    name=input('Name:')
    age=input('Age:')
    # sql="insert into class (name,age,date) values ('%s',%s,now());"%(name,age)
    sql = "insert into class (name,age,date) values (%s,%s,now());"
    cur.execute(sql,[name,age])
    db.commit()
except Exception as e:
    db.rollback()   #退回到commit执行之前的数据库状态
    print(e)

#关闭数据库
cur.close()
db.close()





