import mysql.connector as myConn
from dotenv import load_dotenv
import os

#loads .env file
load_dotenv('.env')

#gets passwords and username from env fole and stores in variable
password: str = os.getenv('PASSWORD')

#establish connection to sql server
mydb = myConn.connect(host = "localhost",user = "root",password = password,database="TestDatabase")
 
#creates cursor
db_cursor = mydb.cursor()

#executes the cursor and creates table
#db_cursor.execute("create table Coins(id int,name varchar(20),value int,year int)")

db_insert = "insert into Coins(id,name,value,year) values(%s,%s,%s,%s)"
db_list = [(2,"republic",10,2020),(3,"independance",1,2013),(4,"independance",2,2009)]

#inserts data
db_cursor.executemany(db_insert,db_list)

#commits the changes
mydb.commit()
print(db_cursor.rowcount,"record inserted")