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

#shows tables
db_cursor.execute("show tables")

for i in db_cursor:
    print(i)

print("created table")

