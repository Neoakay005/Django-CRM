# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345'
)

# prepare a curosr object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE akayco")
print("Database Created!")