import pymysql.cursors
connection = pymysql.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo1',
                        cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    sql = "select * from student "
    cursor.execute(sql)
    result=cursor.fetchone()
    print(result)
