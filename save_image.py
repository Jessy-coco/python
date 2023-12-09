"""
python
mysql数据库存图片的读写操作
"""
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
#创建文件操作对象
# f=open('1.jfif','rb')
# data = f.read()
# #写数据库
# try:
#     sql="update class set image=%s where name='典韦';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()   #退回到commit执行之前的数据库状态
#     print(e)
sql="select image from class where name='典韦';"
cur.execute(sql)
data=cur.fetchone()
with open('1.gif','wb') as f:
    f.write(data[0])

#关闭数据库
cur.close()
db.close()
