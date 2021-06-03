# db_func : Database Functionality
# This files is contains functions that access and manipulate the database

# Creator : Edel Barcenas
# Date : 5/29/21
# Course : CS490

import mysql.connector

#this code is here just for the initialization from this file, and for __connect() and __disconnect() which DONT WORK UGGGHHH
db = mysql.connector.connect(
                host="us-cdbr-east-04.cleardb.com",
                user="be3c5020bf5627",
                password="3bfc3cfa",
                database="heroku_f7729a769a3bca5"
        )
myCursor = db.cursor() 


__drop_table_commands = {}      # { table name : SQL command to drop table }
__init_table_commands = {}      # { table name : SQL command to initialize table }



def __connect():
        db = mysql.connector.connect(
                host="us-cdbr-east-04.cleardb.com",
                user="be3c5020bf5627",
                password="3bfc3cfa",
                database="heroku_f7729a769a3bca5"
        )
        
        myCursor = db.cursor()          #creates object to access and manipulate db

        
def __disconnect():
        myCursor.close()
        db.close()

def __runQuery(query, data):
        #__connect()
        
        db = mysql.connector.connect(
                host="us-cdbr-east-04.cleardb.com",
                user="be3c5020bf5627",
                password="3bfc3cfa",
                database="heroku_f7729a769a3bca5"
        )
        myCursor = db.cursor() 
        
        myCursor.execute(query, data)
        db.commit()
        
        __disconnect()

def __setTableCommands(): # fills the __drop_table_commands & __init_table_commands dictionaries
        
        __drop_table_commands["COMMENT"] = "DROP TABLE IF EXISTS COMMENT;" 
        __drop_table_commands["DM"] = "DROP TABLE IF EXISTS DM;"
        __drop_table_commands["FOLLOW"] = "DROP TABLE IF EXISTS FOLLOW;"
        __drop_table_commands["POST"] = "DROP TABLE IF EXISTS POST;" 
        __drop_table_commands["USER"] = "DROP TABLE IF EXISTS USER;"
 
        __init_table_commands["USER"] = ("CREATE TABLE USER("	
                                                "fname          VARCHAR(20)     NOT NULL,"
	                                        "lname          VARCHAR(20)     NOT NULL,"
	                                        "username       VARCHAR(20)     NOT NULL,"
	                                        "password       VARCHAR(20),"
	                                        "email          VARCHAR(20),"
	                                        "admin_status   SMALLINT        NOT NULL,"
	                                        "block_status   SMALLINT        NOT NULL,"
	                                        "PRIMARY KEY(username) );")
	                                
        __init_table_commands["FOLLOW"] = ("CREATE TABLE FOLLOW("
	                                        "follower       VARCHAR(20)   NOT NULL,"
	                                        "target         VARCHAR(20)   NOT NULL,"
	                                        "FOREIGN KEY(follower) REFERENCES USER(username) ON DELETE CASCADE ON UPDATE CASCADE ,"
	                                        "FOREIGN KEY(target) REFERENCES USER(username)  ON DELETE CASCADE ON UPDATE CASCADE,"
	                                        "PRIMARY KEY(follower, target) );")
	                                        
        __init_table_commands["POST"] = ""
        __init_table_commands["COMMENT"] = ""
        __init_table_commands["DM"] = ""
        
def __initDB(): # drops existing Tables and then re-initializes them using __drop_table_commands & __init_table_commands
        __setTableCommands();
        
        __connect()
        
        for table in __drop_table_commands: 
                myCursor.execute( __drop_table_commands[table] )

        for table in __init_table_commands:
                temp_string = __init_table_commands[table]
                myCursor.execute(temp_string)
                        
        __disconnect()
        
        
        
def addUser(fname, lname, username, password, email, isAdmin):

        add_user = 'INSERT INTO USER VALUES (%s, %s, %s, %s, %s, %s, "0" );'
        user_data = (fname, lname, username, password, email, isAdmin)
        
        __runQuery(add_user , user_data); 

def addFollow(follower, target):
        
        add_follow = 'INSERT INTO FOLLOW VALUES (%s, %s);'
        names = (follower, target);
        
        __runQuery(add_follow, names);



def deleteUser(username):
        query = 'DELETE FROM USER WHERE username = "'+username+'";'
        __runQuery(query, "")



def __getUserInfo(username): #return tuple : ( fname, lname, username, pswrd, email, admin?, blocked? )
        __connect()
        
        db = mysql.connector.connect(
                host="us-cdbr-east-04.cleardb.com",
                user="be3c5020bf5627",
                password="3bfc3cfa",
                database="heroku_f7729a769a3bca5"
        )
        myCursor = db.cursor() 
        
        ret = 0
        
        get_info = 'SELECT * FROM USER WHERE USERNAME = "'+username+'";'
        myCursor.execute( get_info )
        for x in myCursor:      # there should be only 1 tuple in myCursor but it wouldn't work without a for loop
               ret = x     # retrieves first/only tuple
               #if >1 tuple, there is duplicate usernames, which is an issue that should've been caught already
        
        __disconnect()
        return ret  
        
def getFname(username):
        return __getUserInfo(username)[0]
        
def getLname(username):
       return __getUserInfo(username)[1]
       
def getPassword(username): #this is definitely super insecure but were gonna work with it for now
        return __getUserInfo(username)[3]
        
def getEmail(username):
        return __getUserInfo(username)[4]

def getAdminStatus(username): #returns 1 if username isAdmin | 0 if not 
        return __getUserInfo(username)[5]
        
def getBlockStatus(username):
        return __getUserInfo(username)[6]

''' IGNORE THIS FUNCTION FOR NOW
def getFollowers(username):
        query = 'SELECT follower FROM FOLLOW WHERE target = "'+username+'";'
        myCursor.execute(query);
        
        ret = ""
        for x in myCursor: 
                ret = ret + x[0] + '\n'
       
        return ret;

'''        



def setFname(username, fname):
        query = 'UPDATE USER SET fname = %s WHERE username = %s;'
        __runQuery( query , (fname , username) )

def setLname(username, lname):
        query = 'UPDATE USER SET lname = %s WHERE username = %s;'
        __runQuery( query , (lname , username) )

def setUsername( old, new ):
        set_username = 'UPDATE USER SET username = %s WHERE username = %s;'
        __runQuery( set_username , ( new , old ) )

def setPassword(username, password):
        query = 'UPDATE USER SET password = %s WHERE username = %s;'
        __runQuery( query , (password , username) )
        
def setEmail(username, email):
        query = 'UPDATE USER SET email = %s WHERE username = %s;'
        __runQuery( query , (email , username) )
        
def setAdminStatus(username, status):
        query = 'UPDATE USER SET admin_status = %s WHERE username = %s;'
        __runQuery( query , (status , username) )
        
def setBlockStatus(username, status):
        query = 'UPDATE USER SET block_status = %s WHERE username = %s;'
        __runQuery( query , (status , username) )



def usernameTaken(username):    # returns 1 if username is already in database | 0 if it is not
        
        if( __getUserInfo(username) ):
                return 1;
        return 0;





#__initDB();


