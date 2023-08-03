import DB.cnx as cnx
import DB.prep as prep

class notes():
    def __init__(self, userID):
        self.userID = userID

    def readNotes(self):

        #sql code for query
        sql = f"SELECT * FROM notes WHERE userID = {self.userID}"

        #execute sql query
        prep.use_DB()
        cnx.cursor.execute(sql)
        print (cnx.cursor.fetchall())

        return None
    
    def addNotes(self, title, body):

        #sql code and data for query
        sql = "INSERT INTO notes VALUES(null, %s, %s, %s)"
        data = (title, body, self.userID)

        #execute sql query
        prep.use_DB()
        cnx.cursor.execute(sql, data)
        cnx.cnx.commit()

        return None

    def delNotes(self, note):

        #sql code and data for query
        sql =   f"DELETE FROM notes WHERE ID = {note} AND userID = {self.userID};"

        #execute sql query
        prep.use_DB()
        cnx.cursor.execute(sql)
        cnx.cnx.commit()
        return None
    
    def modNotes(self):
        return None