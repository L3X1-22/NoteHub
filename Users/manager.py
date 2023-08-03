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


    #This method hashes the password
    def hash_password(self):
        passh = hashlib.new('SHA256')
        password = self.password.encode()
        passh.update(password)
        self.password = passh.hexdigest()


    #this function register new users into the DB
    def register(self):

        #create hash for the password
        self.hash_password()

        #Data and sql query for new user
        newUser = (self.name, self.lastName, self.email, self.password, datetime.date.today())
        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"

        #Add user to DB
        prep.use_DB()
        cnx.cursor.execute(sql, newUser)
        cnx.cnx.commit()


    #this function allows users to login into their accounts
    def login(self):

        #create hash for the password
        self.hash_password()

        #Data and sql query for searching the user
        searchUser = (self.email, self.password)
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        #Search user in DB
        prep.use_DB()
        cnx.cursor.execute(sql, searchUser)
        result = cnx.cursor.fetchone()
        
        return result[1]