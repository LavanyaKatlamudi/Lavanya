import pymysql
db = pymysql.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo1',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()

query = "CREATE TABLE account (fname varchar(50),lname varchar(50),accno varchar(10))"


try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()
