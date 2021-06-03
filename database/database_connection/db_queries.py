###import the database function
import database.db_func as db


###check if username is taken
def usernameTaken():
    username = request.form["username"]
    password = request.form["password"]

    if db.usernameTaken(username):
        return ("taken.html")
    else:
        db.addUser('NULL', 'NULL', username, password, 'NULL', 0)
        user_data = (fname, lname, username, password, email, isAdmin)
        return ("login.html")
    



###check if email is valid during registration
<h1>Registration</h1>
<h2>Email:
        <br><input type="email" name="email"/>
</h2>

###check if username exists
username = request.db["username"]
if db.usernameTaken(username):
        return(user.html)
        
###check if password matches
password = request.db["password"]
if db.getPassword(password):
        return(user.html)
        
###check if person is admin or not
if db.getAdminStatus(username) == 0: 
                return ("user.html")

else:
        if db.getAdminStatus(username) == 1:
                return("admin.html")
        