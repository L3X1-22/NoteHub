import DB.cnx as cnx
import DB.prep as prep
import datetime
import hashlib

class user:
    def __init__(self, name, lastName, email, password):
        self.name = name
        self.lastName = lastName
        self.email = email
        self.password = password
        self.cursor = cnx.cursor

    #this function register new users into the DB
    def register(self):

        #create hash for password

        passh = hashlib.new('SHA256')
        password = self.password.encode()
        passh.update(password)
        passh = passh.hexdigest()

        #Data and sql query for new user
        newUser = (self.name, self.lastName, self.email, passh, datetime.date.today())
        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"

        #Add user to DB
        prep.use_DB()
        cnx.cursor.execute(sql, newUser)
        cnx.cnx.commit()

        return(self)
    
    #this function allows users to login into their accounts
    def login(self):
        return(self)
    
    