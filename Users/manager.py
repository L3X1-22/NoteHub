import DB.cnx as cnx
import datetime

class user:
    def __init__(self, name, lastName, email, password):
        self.name = name
        self.lastName = lastName
        self.email = email
        self.password = password
        self.cursor = cnx.cursor

    #this function register new users into the DB
    def register(self):
        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        newUser = (self.name, self.lastName, self.email, self.password, datetime.date.today())

        cnx.cursor.execute("use notehub")
        cnx.cursor.execute(sql, newUser)
        cnx.cnx.commit()

        return(self)
    
    #this function allows users to login into their accounts
    def login(self):
        return(self)
    
    