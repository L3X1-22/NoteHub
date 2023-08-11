import Users.manager
import Notes.manager

userID = None
#starting the note app
print('welcome to notehub! \n we are glad that you decided to choose us <3\n')

action = input('what do you want to do? \nlogin(1)\nregister(2)\n')

if action == '1':
    while userID == None:
        print('\nplease tell us who are you!!!\n')
        email = input('\nemail:\n')
        password = input('\npassword:\n')

        user = Users.manager.user('', '', email, password)
        userID = user.login()

elif action == '2':
    while userID == None:
        print('\nLets start with the basics!!')

        name = input('\nname:\n')
        lastName = input('\nlast name:\n')
        email = input('\nemail:\n')
        password = input('\npassword (remember to write a strong password <3):\n')

        user = Users.manager.user(name, lastName, email, password)
        userID = user.register()

user = Notes.manager.notes(userID)

def searchNotes():
    noteCounter = 0
    for i in user.readNotes():
        noteCounter = noteCounter +1
        print('--------------')
        print(f'Note number {noteCounter}')
        print(f'Title: {i[1]}')
        print(f'Body: {i[2]}')
    print('--------------')

action = None

while action != '5':
    
    print('\nAlright! now what you want to do next?\n\n-Add note(1)\n-Read notes(2)\n-Modify note(3)\n-Delete note(4)\n-exit(5)')
    action = input()
    
    if action == '1':
        title = input('\nPlease write the title of the note here:\n')
        body = input('\nPlease write the body of the note here:\n')
        print(user.addNotes(title, body))
        

    elif action == '2':
        print('\nyour great notes are as following:\n')
        searchNotes()
    elif action == '3':
        print('\nplease tell us which one of your notes you want to modify:\n')
        searchNotes()

        noteTitle = input('\nPlease write the note title:\n')
        isTitle = ""

        while isTitle == "":
            title = input('\nPlease tell us if you want to modify the title(1) or the body(2):\n')
            if title == '1':
                isTitle = True
            elif title == '2':
                isTitle = False
            else:
                print('\nyou have to write eather 1 or 2\n')
        
        modification = input('\nPlease tell us how you want to modify it:\n')
        user.modNotes(isTitle, noteTitle, modification)

    elif action == '4':
        print('\nwhich note do you want to delete?:')
        searchNotes()
        note = input('\nPlease write the title of the note that you want to delete:\n')
        user.delNotes(note)

    elif action == '5':
        print('goodbye!! remember to drink water, we love youuu!!! <3')

    else:
        print('you didnt choose a valid option, please choose a valid one!!! <3')