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


#variable to update data
db_delete = "delete from TestDatabase.Coins where id=%s"

#value to be updated to
db_value = (2,)

#executes and deletes value
db_cursor.execute(db_delete,db_value)

#commits the changes
mydb.commit()

print(db_cursor.rowcount,"record deleted")

mydb.close()