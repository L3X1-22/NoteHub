import mysql.connector

cnx = mysql.connector.connect(
host = "localhost",
user = "root",
password = "1234",
buffered = True
)

cursor = cnx.cursor()