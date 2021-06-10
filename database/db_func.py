# db_func : Database Functionality
# This files is contains functions that access and manipulate the database

# Creator : Edel Barcenas
# Created : 5/29/21
# Last Updated : 6/3/21
# Course : CS490

import mysql.connector
from datetime import datetime



__drop_table_commands = {}      # { table name : SQL command to drop table }
__init_table_commands = {}      # { table name : SQL command to initialize table }

def __connector():
        db_con = mysql.connector.connect(
                host="us-cdbr-east-04.cleardb.com",
                user="be3c5020bf5627",
                password="3bfc3cfa",
                database="heroku_f7729a769a3bca5"
        )
        
        return db_con;

def __setTableCommands(): # fills the __drop_table_commands & __init_table_commands dictionaries
        
        __drop_table_commands["COMMENT"] = "DROP TABLE IF EXISTS COMMENT;" 
        __drop_table_commands["DM"] = "DROP TABLE IF EXISTS DM;"
        __drop_table_commands["FOLLOW"] = "DROP TABLE IF EXISTS FOLLOW;"
        __drop_table_commands["POST"] = "DROP TABLE IF EXISTS POST;" 
        __drop_table_commands["USER"] = "DROP TABLE IF EXISTS USER;"
 
        __init_table_commands["USER"] = ("CREATE TABLE USER("	
                                                "fname          VARCHAR(20)             NOT NULL,"
	                                        "lname          VARCHAR(20)             NOT NULL,"
	                                        "username       VARCHAR(20)             NOT NULL,"
	                                        "password       VARCHAR(20),"
	                                        "email          VARCHAR(20),"
	                                        "admin_status   SMALLINT                NOT NULL,"
	                                        "block_status   SMALLINT                NOT NULL,"
	                                        "PRIMARY KEY(username) );")
	                                
        __init_table_commands["FOLLOW"] = ("CREATE TABLE FOLLOW("
	                                        "follower       VARCHAR(20)             NOT NULL,"
	                                        "target         VARCHAR(20)             NOT NULL,"
	                                        "FOREIGN KEY(follower) REFERENCES USER(username) ON DELETE CASCADE ON UPDATE CASCADE ,"
	                                        "FOREIGN KEY(target) REFERENCES USER(username)  ON DELETE CASCADE ON UPDATE CASCADE,"
	                                        "PRIMARY KEY(follower, target) );")
	                                        
        __init_table_commands["POST"] = ("CREATE TABLE POST("
                                                "post_id        INT 	                AUTO_INCREMENT,"
                                                "poster		VARCHAR(20) 	        NOT NULL,"
                                                "song_title	VARCHAR(30) 	        NOT NULL,"
                                                "artist		VARCHAR(30)		NOT NULL,"
                                                "song_link	VARCHAR(100)		NOT NULL,"
                                                "image		VARCHAR(100)		NOT NULL,"
                                                "caption 	VARCHAR(500),"
                                                "ptime		TIMESTAMP       	NOT NULL,"
                                                "FOREIGN KEY(poster) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,"
                                                "PRIMARY KEY(post_id) );")
                                                
        __init_table_commands["COMMENT"] = ("CREATE TABLE COMMENT("
                                                "com_id		INT			AUTO_INCREMENT,"
                                                "sender		VARCHAR(20)		NOT NULL,"
                                                "post_id	INT			NOT NULL,"
                                                "message 	VARCHAR(500)		NOT NULL,"
                                                "ctime		TIMESTAMP		NOT NULL,"
                                                "FOREIGN KEY(sender) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,"
                                                "FOREIGN KEY(post_id) REFERENCES POST(post_id) ON DELETE CASCADE,"
                                                "PRIMARY KEY(com_id) );")
                                                
        __init_table_commands["DM"] = ("CREATE TABLE DM("
                                                "msg_id		INT 			AUTO_INCREMENT,"
                                                "sender		VARCHAR(20) 		NOT NULL,"
                                                "receiver	VARCHAR(20) 		NOT NULL,"
                                                "message	VARCHAR(500),"
                                                "dtime		TIMESTAMP		NOT NULL,"
                                                "FOREIGN KEY(sender) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,"
                                                "FOREIGN KEY(receiver) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,"
                                                "PRIMARY KEY(msg_id) );")
        
def __initDB(): # drops existing Tables and then re-initializes them using __drop_table_commands & __init_table_commands
        
        __setTableCommands();
        db_con = __connector()
        myCursor = db_con.cursor()
            
                
        for table in __drop_table_commands: 
                myCursor.execute( __drop_table_commands[table] )

        for table in __init_table_commands:
                temp_string = __init_table_commands[table]
                myCursor.execute(temp_string)
                
                
        myCursor.close()
        db_con.close()

#__initDB();



def __queryCommit(query, data):
       
        db_con = __connector()
        myCursor = db_con.cursor()
        
        myCursor.execute(query, data)
        db_con.commit()
        
        db_con.close()
        myCursor.close()

def __queryTuple(query, data):
        
        db_con = __connector()
        myCursor = db_con.cursor()
        ret = [];
        
        myCursor.execute(query, data)
        for x in myCursor:      # there should be only 1 tuple in myCursor but it wouldn't work without a for loop
               ret = x     # retrieves first/only tuple
               #if >1 tuple, there is duplicate usernames, which is an issue that should've been caught already
        
        db_con.close()
        myCursor.close()
        return ret

def __queryArray(query, data):
        db_con = __connector()
        myCursor = db_con.cursor()
        array = [];
        
        myCursor.execute(query, data)
        for x in myCursor:     
                array.append(x[0])
        db_con.close()
        myCursor.close()
                
        return array


        
def addComment(sender, post_id, message):
        query = 'INSERT INTO COMMENT(sender, post_id, message, ctime) VALUES(%s, %s, %s, %s );'
        comment_time = str(datetime.now())[:19]         #gets current time
        values = ( sender, str(post_id), message, comment_time )
        __queryCommit( query , values )      
        
def addDM( sender, receiver, message):
        query = 'INSERT INTO DM(sender, receiver, message, dtime) VALUES(%s, %s, %s, %s);'
        dm_time = str(datetime.now())[:19]              #gets current time
        values = ( sender, receiver, message, dm_time )
        __queryCommit( query , values)

def addFollow(follower, target):
        
        add_follow = 'INSERT INTO FOLLOW VALUES (%s, %s);'
        names = (follower, target);
        
        __queryCommit(add_follow, names);
        
def addUser(fname, lname, username, password, email, isAdmin):

        query = 'INSERT INTO USER VALUES (%s, %s, %s, %s, %s, %s, "0" );'
        user_data = (fname, lname, username, password, email, isAdmin)
        
        __queryCommit(query , user_data); 

def addPost(poster, song_title, artist, song_link, image, caption):
        
        query = 'INSERT INTO POST(poster, song_title, artist, song_link, image, caption, ptime ) VALUES(%s, %s, %s, %s, %s, %s, %s);'
        post_time =  str(datetime.now())[:19]           #gets current time
        data = ( poster, song_title, artist, song_link, image, caption, post_time )
        __queryCommit(query, data)



def deleteUser(username):
        query = 'DELETE FROM USER WHERE username = "'+username+'";'
        __queryCommit(query, "")

def deleteComment(com_id):
        query = 'DELETE FROM COMMENT WHERE com_id = '+str(com_id)+';'
        __queryCommit(query, "")
        
def deleteFollow(follower, target):
        query = 'DELETE FROM FOLLOW WHERE (follower = %s AND target = %s)'
        values = (follower, target)
        __queryCommit(query, values)

def deletePost(post_id):
        query = 'DELETE FROM POST WHERE com_id = '+str(post_id)+';'
        __queryCommit(query, "")



def __getUserInfo(username): #return tuple : ( fname, lname, username, pswrd, email, admin?, blocked? )
        query = 'SELECT * FROM USER WHERE username = "'+username+'";'
        return __queryTuple(query, "" )
        
def getFname(username):
        return __getUserInfo(username)[0];
        
def getLname(username):
       return __getUserInfo(username)[1];
       
def getPassword(username): #this is definitely super insecure but were gonna work with it for now
        return __getUserInfo(username)[3];
        
def getEmail(username):
        return __getUserInfo(username)[4];

def getAdminStatus(username): #returns 1 if username isAdmin | 0 if not 
        return __getUserInfo(username)[5];
        
def getBlockStatus(username):
        return __getUserInfo(username)[6];

def getFollowers(username):
        query = 'SELECT follower FROM FOLLOW WHERE target = "'+username+'";';
        
        array = __queryArray(query, "");               #array of usernames
        
        return array;     

def getComments(post_id):
        query = 'SELECT com_id FROM COMMENT WHERE post_id = '+str(post_id)+' ORDER BY ctime;';
        array = __queryArray(query, "");
        
        return array;
        
def getConvo(user1, user2):
        query = 'SELECT msg_id FROM DM WHERE (sender = %s AND receiver = %s) OR (sender = %s AND receiver = %s) ORDER BY dtime;';
        values = (user1, user2, user2, user1);
        
        array = __queryArray(query, values);
        
        return array;
        
def getPosts(username):
        query = 'SELECT post_id FROM POST WHERE poster = "'+username+'" ORDER BY ptime;';
        array = __queryArray(query, "");
        
        return array;

def getTimeCreated(entity, id_number) : # entity : (p : post), (c : comment), (d : direct message)
        
        if entity == 'p' :
                query = "SELECT ptime FROM POST WHERE post_id = "+str(id_number)+" ;";
        elif entity == 'c' :
                query = "SELECT ctime FROM COMMENT WHERE com_id = "+str(id_number)+" ;";
        elif entity == 'd' : 
                query = "SELECT dtime FROM DM WHERE msg_id = "+str(id_number)+" ;";
        else : 
                raise Exception("Invalid Arg 'entity' in getTimeCreated(id_number, entity) :"
                                "\nTry ( 'p' : POST ) , ( 'c' : COMMENT ) , ( 'd' : DIRECT_MESSAGE");
        
        ret = __queryTuple(query, "");
        
        if ret : 
                return ret[0];
        else :
                raise Exception("Entity identifier '"+entity+"' does not have"
                                " any instances with id_number "+str(id_number));

def getCreator(entity, id_number) :  # entity : (p : post), (c : comment), (d : direct message)
        
        if entity == 'p' :
                query = "SELECT poster FROM POST WHERE post_id = "+str(id_number)+" ;";
        elif entity == 'c' :
                query = "SELECT sender FROM COMMENT WHERE com_id = "+str(id_number)+" ;";
        elif entity == 'd' : 
                query = "SELECT sender FROM DM WHERE msg_id = "+str(id_number)+" ;";
        else : 
                raise Exception("Invalid Arg 'entity' in getCreator(id_number, entity) :"
                                "\nTry ( 'p' : POST ) , ( 'c' : COMMENT ) , ( 'd' : DIRECT_MESSAGE");
        
        ret = __queryTuple(query, "");
        
        if ret : 
                return ret[0];
        else :
                raise Exception("Entity identifier '"+entity+"' does not have"
                                " any instances with id_number "+str(id_number));
                                
def getText(entity, id_number) :  # entity : (p : post), (c : comment), (d : direct message)
        
        if entity == 'p' :
                query = "SELECT caption FROM POST WHERE post_id = "+str(id_number)+" ;";
        elif entity == 'c' :
                query = "SELECT message FROM COMMENT WHERE com_id = "+str(id_number)+" ;";
        elif entity == 'd' : 
                query = "SELECT message FROM DM WHERE msg_id = "+str(id_number)+" ;";
        else : 
                raise Exception("Invalid Arg 'entity' in getText(id_number, entity) :"
                                "\nTry ( 'p' : POST ) , ( 'c' : COMMENT ) , ( 'd' : DIRECT_MESSAGE");
        
        ret = __queryTuple(query, "");
        if ret : 
                return ret[0];
        else :
                raise Exception("Entity identifier '"+entity+"' does not have"
                                " any instances with id_number "+str(id_number));

def getSongTitle(post_id) : 
        return __getPostInfo(post_id)[2];
        
def getArtist(post_id) : 
        return __getPostInfo(post_id)[3];
        
def getSongLink(post_id) : 
        return __getPostInfo(post_id)[4];
        
def getImageLink(post_id) : 
        return __getPostInfo(post_id)[5];
        
def __getPostInfo(post_id) : 
        query = 'SELECT * FROM POST WHERE post_id = '+str(post_id)+';'
        return __queryTuple(query, "");
        
        

#POSTS:  song_title, artist, song_link, image, caption 

def setFname(username, fname):
        query = 'UPDATE USER SET fname = %s WHERE username = %s;'
        __queryCommit( query , (fname , username) )

def setLname(username, lname):
        query = 'UPDATE USER SET lname = %s WHERE username = %s;'
        __queryCommit( query , (lname , username) )

def setUsername( old, new ):
        query = 'UPDATE USER SET username = %s WHERE username = %s;'
        __queryCommit( query , ( new , old ) )

def setPassword(username, password):
        query = 'UPDATE USER SET password = %s WHERE username = %s;'
        __queryCommit( query , (password , username) )
        
def setEmail(username, email):
        query = 'UPDATE USER SET email = %s WHERE username = %s;'
        __queryCommit( query , (email , username) )
        
def setAdminStatus(username, status):
        query = 'UPDATE USER SET admin_status = %s WHERE username = %s;'
        __queryCommit( query , (status , username) )
        
def setBlockStatus(username, status):
        query = 'UPDATE USER SET block_status = %s WHERE username = %s;'
        __queryCommit( query , (status , username) )


# I know search Users can be used for this, but it was created after the middle man implemented usernameTaken()
def usernameTaken(username):    # returns 1 if username is already in database | 0 if it is not
        
        if( __getUserInfo(username) ):
                return 1;
        return 0;
                
        

def searchUsers(search):
        query = "SELECT username FROM USER WHERE SUBSTRING(username, 1, %s) = %s ORDER BY username;";
        array = __queryArray(query, (str(len(search)), search));
        return array;
        
def searchPosts(search):
        search_len = str(len(search));
        query = "SELECT post_id FROM POST WHERE (SUBSTRING(artist, 1, %s) = %s) OR (SUBSTRING(song_title, 1, %s) = %s) ORDER BY ptime;";
        values = (search_len, search, search_len, search);
        array = __queryArray(query, values);
        return array;
        
        