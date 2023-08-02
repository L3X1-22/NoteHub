import DB.cnx as cnx

cursor = cnx.cursor

def prep():    
    cursor.execute("""

    CREATE DATABASE IF NOT EXISTS notehub;

    use notehub;
                     
    CREATE TABLE IF NOT EXISTS users(             
        ID int auto_increment not null,
        name varchar(255) not null,
        lastName varchar(255) not null,
        email varchar(255),
        password varchar(255),
        userDate date,
        PRIMARY KEY(ID)
    );
        
    CREATE TABLE IF NOT EXISTS notes(
        ID int auto_increment not null,
        title varchar(255) not null,
        body varchar(255) not null,
        userID int,
        PRIMARY KEY(ID),
        FOREIGN KEY(userID) REFERENCES users(ID)
    );

    """)

def use_DB():
    cursor.execute('use notehub;')