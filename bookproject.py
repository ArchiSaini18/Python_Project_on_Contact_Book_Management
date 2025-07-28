import pymysql
conn=pymysql.connect(host="localhost" ,user="root", password="1234")
cur=conn.cursor()
#cur.execute("Create database contact")
print("Database created")


conn=pymysql.connect(host="localhost" ,user="root", password="1234",
db="contact")
a=conn.cursor()
a.execute('''CREATE TABLE BOOK(NAME CHAR(20) PRIMARY KEY NOT NULL,
ADDRESS CHAR(100),MOBILE BIGINT,EMAIL VARCHAR(20))''')
print("table created sucessfully!!")

conn.close()
1234
    
