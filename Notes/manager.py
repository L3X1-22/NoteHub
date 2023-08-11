import DB.cnx as cnx

class notes():
    def __init__(self, userID):
        self.userID = userID

    def readNotes(self):

        #sql code for query
        sql = f"SELECT * FROM notes WHERE userID = {self.userID}"

        #execute sql query
        cnx.cursor.execute(sql)

        return cnx.cursor.fetchall()
    
    def addNotes(self, title, body):

        #sql code and data for query
        sql = "INSERT INTO notes VALUES(null, %s, %s, %s)"
        data = (title, body, self.userID)

        #execute sql query
        cnx.cursor.execute(sql, data)
        cnx.cnx.commit()

        return 'Note added succesfully!'

    def delNotes(self, note):

        #sql code and data for query
        sql =   f"DELETE FROM notes WHERE title = '{note}' AND userID = {self.userID};"

        #execute sql query
        cnx.cursor.execute(sql)
        cnx.cnx.commit()
        if cnx.cursor.rowcount == 0:
            self.delNotes(input('\nWrite correctly the title of the note that you want to delete please!!\n\nNote title:\n'))
        if cnx.cursor.rowcount == 0:
            return 'Note deleted'
    
    def modNotes(self, isTitle, title, userInput):
        #sql code and data for query
        if isTitle:
            sql = "UPDATE notes SET title = %s where userID = %s and title = %s"
        else:
            sql = "UPDATE notes SET body = %s where userID = %s and title = %s"
        data = (userInput, self.userID, title)

        #execute sql query
        cnx.cursor.execute(sql, data)
        cnx.cnx.commit()
        if cnx.cursor.rowcount == 0:
            print('Wrong title!!! if you have troubles writing it please copy and paste the title')
            self.modNotes(isTitle, input('\nPlease write the note title:\n'), userInput)
        if cnx.cursor.rowcount >=1:
            return 'Note modified succesfully!!!'