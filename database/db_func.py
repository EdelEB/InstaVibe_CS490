# db_func : Database Functionality
# This files is contains functions that access and manipulate the database

# Creator : Edel Barcenas
# Created : 5/29/21
# Last Updated : 6/3/21
# Course : CS490

import mysql.connector
from datetime import datetime


def __connector():
        db_con = mysql.connector.connect(
                host="us-cdbr-east-04.cleardb.com",
                user="b600fe51c41038",
                password="f2ad2d79",
                database="heroku_3c9e97a749311b6"
        )
        
        return db_con;

def __sqlFileToCommands(file_name):
    sql_file = open(file_name, "r");
    
    curr_string = "";
    command_arr = [];
    
    for line in sql_file:
        no_comments = line.split("--")[0];
        
        for char in no_comments:
            
            if(char == ';'):
                curr_string = curr_string + char;
                command_arr.append(curr_string);
                curr_string = "";
                
            elif(char == '\t' or char == '\n'):
                curr_string = curr_string + ' ';
                
            else:
                curr_string = curr_string + char;
                
    sql_file.close();
    
    return command_arr;
        
def __initDB(): # drops existing Tables and then re-initializes them using __drop_table_commands & __init_table_commands
        
        db_con = __connector()
        myCursor = db_con.cursor()
                  
        for command in __sqlFileToCommands("/home/ec2-user/environment/database/initTables.sql"):
                myCursor.execute(command);     
                
        myCursor.close()
        db_con.close()

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

def __queryTupleArray(query, data):
        db_con = __connector()
        myCursor = db_con.cursor()
        array = [];
        
        myCursor.execute(query, data)
        for x in myCursor:     
                array.append(x)
        db_con.close()
        myCursor.close()
                
        return array

        
def addComment(sender, post_id, message):
        query = 'INSERT INTO COMMENT(sender, post_id, message, ctime) VALUES(%s, %s, %s, %s );'
        comment_time = str(datetime.now())[:19]         #gets current time
        values = ( sender, str(post_id), message, comment_time )
        __queryCommit( query , values )      
        
def addConvo(user1, user2):
        query = 'INSERT INTO CONVERSATION(user1, user2, new_message) VALUES(%s, %s, 0);';
        values = (user1, user2);
        __queryCommit( query , values );

def addMessage( convo_id, sender, receiver, message):
        query = 'INSERT INTO Message(convo_id, sender, receiver, message, mtime, is_read) VALUES(%s, %s, %s, %s, %s, 0);';
        mtime = str(datetime.now())[:19];              #gets current time
        values = ( convo_id, sender, receiver, message, mtime );
        __queryCommit( query , values);

def addFollow(follower, target):
        
        add_follow = 'INSERT INTO FOLLOW VALUES (%s, %s);'
        names = (follower, target);
        
        __queryCommit(add_follow, names);
        
def addUser(fname, lname, username, password, email, isAdmin):

        query = 'INSERT INTO USER VALUES (%s, %s, %s, %s, %s, %s, "0" );'
        user_data = (fname, lname, username, password, email, isAdmin)
        
        __queryCommit(query , user_data); 

def addPost(poster, song_title, artist, song_link, image, caption, lyric_link):
        
        query = 'INSERT INTO POST(poster, song_title, artist, song_link, image, caption, ptime, lyric_link ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);'
        post_time =  str(datetime.now())[:19]           #gets current time
        data = ( poster, song_title, artist, song_link, image, caption, post_time, lyric_link )
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


def anyNewMessages(convo_id):
        query = 'SELECT new_message FROM CONVERSATION WHERE convo_id = %s;';
        return __queryTuple(query, convo_id);


def getUserInfo(username): #return tuple : ( fname, lname, username, pswrd, email, admin?, blocked? )
        query = 'SELECT * FROM USER WHERE username = "'+username+'";'
        return __queryTuple(query, "" )

def getPostInfo(post_id) : 
        query = 'SELECT * FROM POST WHERE post_id = '+str(post_id)+' ;';
        return __queryTuple(query, ''); #POSTS:  song_title, artist, song_link, image, caption 

def getFname(username):
        return getUserInfo(username)[0];
        
def getLname(username):
       return getUserInfo(username)[1];
       
def getPassword(username): #this is definitely super insecure but were gonna work with it for now
        return getUserInfo(username)[3];
        
def getEmail(username):
        return getUserInfo(username)[4];

def getAdminStatus(username): #returns 1 if username isAdmin | 0 if not 
        return getUserInfo(username)[5];
        
def getBlockStatus(username):
        return getUserInfo(username)[6];

def getFollowers(username):
        query = 'SELECT follower FROM FOLLOW WHERE target = "'+username+'";';
        
        array = __queryArray(query, "");               #array of usernames
        
        return array;     

def getComments(post_id):
        query = 'SELECT com_id FROM COMMENT WHERE post_id = '+str(post_id)+' ORDER BY ctime;';
        array = __queryArray(query, "");
        
        return array;
        
def getConvos(user):
        query = 'SELECT user1, user2 FROM CONVERSATION WHERE (user1 = %s OR user2 = %s);';
        values = ( user, user );
        array = __queryTupleArray(query, values);
        
        return array;
        
def getConvoId(user1, user2):
        query = 'SELECT convo_id FROM CONVERSATION WHERE (user1 = %s AND user2 = %s) OR (user1 = %s AND user2 = %s);';
        values = (user1, user2, user2, user1);
        
        ret = __queryTuple(query, values);
        
        try:
                return ret[0];
        except:
                return -1; # no convo exists
        
def getMessages(convo_id):
        query = 'SELECT msg_id FROM MESSAGE WHERE convo_id = ' +str(convo_id)+ ' ORDER BY mtime';
        array = __queryArray(query, "");
        
        return array;

def getMessagesTuples(convo_id):
        query = 'SELECT * FROM MESSAGE WHERE convo_id = ' +str(convo_id)+ ' ORDER BY mtime';
        array = __queryTupleArray(query, "");
        
        return array;
        
def getPosts(username):
        query = 'SELECT post_id FROM POST WHERE poster = "'+username+'" ORDER BY ptime;';
        array = __queryArray(query, "");
        
        return array;

def getTimeCreated(entity, id_number) : # entity : (p : post), (c : comment), (m : message)
        
        if entity == 'p' :
                query = "SELECT ptime FROM POST WHERE post_id = "+str(id_number)+" ;";
        elif entity == 'c' :
                query = "SELECT ctime FROM COMMENT WHERE com_id = "+str(id_number)+" ;";
        elif entity == 'm' : 
                query = "SELECT mtime FROM MESSAGE WHERE msg_id = "+str(id_number)+" ;";
        else : 
                raise Exception("Invalid Arg 'entity' in getTimeCreated(id_number, entity) :"
                                "\nTry ( 'p' : POST ) , ( 'c' : COMMENT ) , ( 'm' : MESSAGE");
        
        ret = __queryTuple(query, "");
        
        if ret : 
                return ret[0];
        else :
                raise Exception("Entity identifier '"+entity+"' does not have"
                                " any instances with id_number "+str(id_number));

def getCreator(entity, id_number) :  # entity : (p : post), (c : comment), (m : message)
        
        if entity == 'p' :
                query = "SELECT poster FROM POST WHERE post_id = "+str(id_number)+" ;";
        elif entity == 'c' :
                query = "SELECT sender FROM COMMENT WHERE com_id = "+str(id_number)+" ;";
        elif entity == 'm' : 
                query = "SELECT sender FROM MESSAGE WHERE msg_id = "+str(id_number)+" ;";
        else : 
                raise Exception("Invalid Arg 'entity' in getCreator(id_number, entity) :"
                                "\nTry ( 'p' : POST ) , ( 'c' : COMMENT ) , ( 'm' : MESSAGE");
        
        ret = __queryTuple(query, "");
        
        if ret : 
                return ret[0];
        else :
                raise Exception("Entity identifier '"+entity+"' does not have"
                                " any instances with id_number "+str(id_number));
                                
def getText(entity, id_number) :  # entity : (p : post), (c : comment), (m : message)
        
        if entity == 'p' :
                query = "SELECT caption FROM POST WHERE post_id = "+str(id_number)+" ;";
        elif entity == 'c' :
                query = "SELECT message FROM COMMENT WHERE com_id = "+str(id_number)+" ;";
        elif entity == 'm' : 
                query = "SELECT message FROM MESSAGE WHERE msg_id = "+str(id_number)+" ;";
        else : 
                raise Exception("Invalid Arg 'entity' in getText(id_number, entity) :"
                                "\nTry ( 'p' : POST ) , ( 'c' : COMMENT ) , ( 'm' : MESSAGE");
        
        ret = __queryTuple(query, "");
        if ret : 
                return ret[0];
        else :
                raise Exception("Entity identifier '"+entity+"' does not have"
                                " any instances with id_number "+str(id_number));

def getSongTitle(post_id) : 
        return getPostInfo(post_id)[2];
        
def getArtist(post_id) : 
        return getPostInfo(post_id)[3];
        
def getSongLink(post_id) : 
        return getPostInfo(post_id)[4];
        
def getImageLink(post_id) : 
        return getPostInfo(post_id)[5];
        
def getLyricLink(post_id) : 
        return getPostInfo(post_id)[8];
        


def setNewMessage(convo_id, num):
        query = 'UPDATE USER SET new_message = %s WHERE convo_id = %s;';
        __queryCommit(query, (num) );
        
def setFname(username, fname):
        query = 'UPDATE USER SET fname = %s WHERE username = %s;';
        __queryCommit( query , (fname , username) );

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
          
# I know search Users can be used for this, but it was created after the middle man implemented usernameTaken()
def usernameTaken(username):    # returns 1 if username is already in database | 0 if it is not
        
        if( getUserInfo(username) ):
                return 1;
        return 0;
      
#def anyUnreadMessage(username):
 #       for name in getFollowers(username):
                
        