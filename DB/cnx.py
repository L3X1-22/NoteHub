import mysql.connector
import DB.prep as prep

#attempt to connect to a database
try:
    cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    buffered = True,
    database = 'notehub'
    )

#if database doesnt exist it's created and connected to it
except mysql.connector.errors.ProgrammingError: 
    #connect to a MySql server
    cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    buffered = True,
    )
    #create database
    prep.prep()
    cnx.close()

    #connect to database created previously
    cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    buffered = True,
    database = 'notehub'
    )

cursor = cnx.cursor()