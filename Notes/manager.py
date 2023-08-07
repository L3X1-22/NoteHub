import DB.cnx as cnx

class notes():
    def __init__(self, userID):
        self.userID = userID

    def readNotes(self):

        #sql code for query
        sql = f"SELECT * FROM notes WHERE userID = {self.userID}"

        #execute sql query
        cnx.cursor.execute(sql)
        print (cnx.cursor.fetchall())

        return None
    
    def addNotes(self, title, body):

        #sql code and data for query
        sql = "INSERT INTO notes VALUES(null, %s, %s, %s)"
        data = (title, body, self.userID)

        #execute sql query
        cnx.cursor.execute(sql, data)
        cnx.cnx.commit()

        return None

    def delNotes(self, note):

        #sql code and data for query
        sql =   f"DELETE FROM notes WHERE ID = {note} AND userID = {self.userID};"

        #execute sql query
        cnx.cursor.execute(sql)
        cnx.cnx.commit()
        return None
    
    def modNotes(self, noteID, isTitle, userInput):
        #sql code and data for query
        if isTitle:
            sql = "UPDATE notes SET title = %s where ID = %s"
        else:
            sql = "UPDATE notes SET body = %s where ID = %s"
        data = (userInput, noteID)

        #execute sql query
        cnx.cursor.execute(sql, data)
        cnx.cnx.commit()
        return None