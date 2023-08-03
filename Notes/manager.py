import DB.cnx as cnx
import DB.prep as prep

class notes():
    def __init__(self, userID):
        self.userID = userID

    def readNotes(self):

        #data and sql code for query
        sql = "SELECT * FROM notes WHERE userID = %s"
        data = (self.userID)

        prep.use_DB()
        cnx.cursor.execute(sql, data)
        print (cnx.cursor.fetchall())
        return None
    
    def addNotes(self):
        return None

    def delNotes(self):
        return None
    
    def modNotes(self):
        return None