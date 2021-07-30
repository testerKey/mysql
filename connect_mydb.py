# caching_sha2_password登录失败解决方法：更改默认登录方式+引入mysql-connector-python
# 提交
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root" ,
  database = "mydatabase"
)
cursor = mydb.cursor()
print(mydb)
print(cursor)
cursor.close()
mydb.close()