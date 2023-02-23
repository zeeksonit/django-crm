import mysql.connector

dataBase = mysql.connector.connect(
        host='localhost',
        user='djangouser',
        passwd='password'
        )

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a dataBase
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
