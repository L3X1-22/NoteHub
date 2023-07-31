import DB.prep
import DB.cnx as database
import Users.manager

#DB.prep.prep()

newUser = Users.manager.user('davis', 'travis', 'travis@travis.com', '1234')
newUser.register()