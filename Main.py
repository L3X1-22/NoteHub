import Users.manager
import Notes.manager


#starting the note app
print('welcome to notehub! \n we are glad that you decided to choose us <3')

action = input('what do you want to do? \n login(1)\nregister(2)')

if action == '1':
    print('\nplease tell us who are you!!!')
    email = input('\nemail:')
    password = input('\npassword:')

    user = Users.manager.user('', '', email, password)

elif action == '2':
    print('\nLets start with the basics!!')

    name = input('\name:')
    lastName = input('\nlast name:')
    email = input('\nemail:')
    password = input('\npassword (remember to write a strong password <3):')

    user = Users.manager.user(name, lastName, email, password)


newUser = Users.manager.user('davis', 'travis', 'travis@travis.com', '1234')
newUser.login()

note = Notes.manager.notes(1)
#note.delNotes(1)
note.addNotes('tercera prueba desde main.py', 'esta es la tercera prueba')
#note.readNotes()
note.modNotes(2, False, "prueba de modificación")
