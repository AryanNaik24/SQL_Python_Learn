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
db_update = "update TestDatabase.Coins set name=%s , value=%s , year=%s where id=%s"

#value to be updated to
db_value = ("mahatmagandhi",2,2012,3)

#executes and updates value
db_cursor.execute(db_update,db_value)

#commits the changes
mydb.commit()

print("updated")
