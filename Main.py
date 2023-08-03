import DB.prep
import DB.cnx as database
import Users.manager
import Notes.manager

#DB.prep.prep()

newUser = Users.manager.user('davis', 'travis', 'travis@travis.com', '1234')
newUser.register()

note = Notes.manager.notes(1)
note.addNotes('primera prueba desde main.py', 'esta es la primera prueba')
note.delNotes(1)
note.readNotes()
