import mysql.connector

def db_preparation():
    cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    buffered = True
    )

    cursor = cnx.cursor()

    cursor.execute("""

    CREATE DATABASE IF NOT EXISTS notehub;

    use notehub;
                     
    CREATE TABLE IF NOT EXISTS users(             
        ID int auto_increment not null,
        nombre varchar(255) not null,
        apellido varchar(255) not null,
        email varchar(255),
        password varchar(255),
        PRIMARY KEY(ID)
    );

    use notehub;              
    CREATE TABLE IF NOT EXISTS notes(
        ID int auto_increment not null,
        title varchar(255) not null,
        body varchar(255) not null,
        userID int,
        PRIMARY KEY(ID),
        FOREIGN KEY(userID) REFERENCES users(ID)
    );

    """)