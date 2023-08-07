import mysql.connector

#this function creates the database
def prep():    
    cursor.execute("""

    CREATE DATABASE IF NOT EXISTS notehub;

    use notehub;
                     
    CREATE TABLE IF NOT EXISTS users(             
        ID int auto_increment NOT NULL,
        name varchar(255) NOT NULL,
        lastName varchar(255) NOT NULL,
        email varchar(255),
        password varchar(255),
        userDate date,
        PRIMARY KEY(ID),
        UNIQUE (email)
    );
        
    CREATE TABLE IF NOT EXISTS notes(
        ID int auto_increment NOT NULL,
        title varchar(255) NOT NULL,
        body varchar(255) NOT NULL,
        userID int,
        PRIMARY KEY(ID),
        FOREIGN KEY(userID) REFERENCES users(ID)
    );

    """)

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
    cursor = cnx.cursor()
    prep()
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