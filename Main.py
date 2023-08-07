import DB.prep
import DB.cnx as database
import Users.manager
import Notes.manager

#DB.prep.prep()

newUser = Users.manager.user('davis', 'travis', 'travis@travis.com', '1234')
newUser.register()

note = Notes.manager.notes(1)
#note.delNotes(1)
note.addNotes('tercera prueba desde main.py', 'esta es la tercera prueba')
#note.readNotes()
note.modNotes(2, False, "prueba de modificación")