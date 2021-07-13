
import pymysql

conn = pymysql.connect(
        host= "database-1.cxhf9fg4vmrw.us-east-2.rds.amazonaws.com", #endpoint link
        port = 3306, # 3306
        user = "admin", # admin
        password = "Group2001", #Pass
        db = "newone", #Database
        
        )

#Tablemaking
# cursor=conn.cursor()
# create_table="""
# create table Details (name varchar(200),age varchar(10) ,email varchar(200),phone varchar(20),rating varchar(30),comment varchar(200))
# """
# cursor.execute(create_table)


def insert_details(name,age,email,phone,rating,comment):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (name,age,email,phone,rating,comment) VALUES (%s,%s,%s,%s,%s,%s)", (name,age,email,phone,rating,comment))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details
