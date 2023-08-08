#imports
import mysql.connector as myConn
from dotenv import load_dotenv
import os

#loads .env file
load_dotenv('.env')

#gets passwords and username from env fole and stores in variable
password: str = os.getenv('PASSWORD')

#establish connection to sql server
mydb = myConn.connect(host = "localhost",user = "root",password = password)
   
   
             
print(mydb,"connection established")

mydb.close()
