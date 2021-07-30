# 导入模块
import mysql.connector

# 打开数据库连接
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root" ,
  database = "mydatabase"
)

# 使用cursor()方法创建一个游标对象cursor
cursor = mydb.cursor()
sql = "SELECT * FROM employee WHERE income > 1000 "
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    for row in results:
        print(row)
        first_name = row[0]
        last_name = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print(first_name, last_name, age, sex, income)
except:
    print('Uable to fetch data!')

# 关闭对象
cursor.close()

# 关闭数据库连接
mydb.close()