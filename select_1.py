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


#executes and selects all elements from the table
db_cursor.execute("select * from TestDatabase.Coins")
#fetches all the elements
# data = db_cursor.fetchall()
for data in db_cursor.fetchall():
    print(data)


