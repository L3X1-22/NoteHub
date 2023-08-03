import DB.cnx as cnx
import DB.prep as prep

class notes():
    def __init__(self, userID):
        self.userID = userID

    def readNotes(self):

        #sql code for query
        sql = f"SELECT * FROM notes WHERE userID = {self.userID}"

        prep.use_DB()
        cnx.cursor.execute(sql)
        print (cnx.cursor.fetchall())
        return None
    
    def addNotes(self):
        return None

    def delNotes(self):
        return None
    
    def modNotes(self):
        return None