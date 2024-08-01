import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="nessaug01db"
)

mycursor = mydb.cursor()
# mycursor.execute("show tables")
# mycursor.execute("create table browser1(browserid varchar(10),browsername varchar(25),browserversion varchar(25))")
mycursor.execute("insert into browser1 values('b012','firefox','120')")

mydb.commit()
# print(mycursor.rowcount)

mycursor.execute("delete from browser1 where browserid='b011'")

mycursor.execute("select * from browser1")
dataset = mycursor.fetchall()

for data in dataset:
    print(data)