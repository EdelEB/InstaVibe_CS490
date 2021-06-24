import requests
import os
import flask
from flask import Flask, render_template, request, session, send_from_directory, json
from dotenv import load_dotenv, find_dotenv
import random
import database.db_func as db
from flask_socketio import SocketIO
from flask_cors import CORS

app = flask.Flask(__name__)

cors = CORS(app, resources={"/*": {"origins": "*"}})

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    manage_session=False
)


AUTH_URL = 'https://accounts.spotify.com/api/token'

load_dotenv(find_dotenv()) # This is to load your API keys from .env

# POST
SPOT_KEY = os.environ['SPOT_KEY']
SPOT_SECRET = os.environ['SPOT_SECRET']
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': SPOT_KEY,
    'client_secret': SPOT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}



@app.route("/")
def main_page():
    return flask.render_template("index.html") #Main page
    
    
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    return flask.render_template("login.html") #Invalid login page




@app.route("/register", methods=['GET', 'POST'])
def register():
    return flask.render_template("register.html") #Registration page
    
    
    
@app.route("/search", methods=['GET', 'POST'])
def search():
    search = request.form["searched_user"]
    post_ids = []
    post_images = []
    search_results = db.searchUsers(search)
    
    if search_results:
        search_user = search_results[0]
        
        post_ids = db.getPosts(search_user)
        if len(post_ids) != 0:
            # print(post_ids)
            for post in post_ids:
                post_images.append(db.getImageLink(post))
            # print(post_images)
        else:
            post_ids = None
            post_images = None
        return flask.render_template("visit.html", 
            user = search_user,
            ids = post_ids,
            snaps = post_images
        )
        
    else:
        return flask.render_template("userDNE.html",
                                    user = username)

    
    
@app.route("/result2", methods=['GET', 'POST'])
def result2():
    username = request.form["username"]
    password = request.form["password"]

    if db.usernameTaken(username): # If username is already taken
        return flask.render_template("taken.html")
    else: # Successful registration takes user to login
        db.addUser('NULL', 'NULL', username, password, 'NULL', 0)
                
        return flask.render_template("login.html",
                                    user = username)
        
        
        
@app.route("/create_post", methods=['GET', 'POST'])
def create_post():
    return flask.render_template("create_post.html")
    

    
@app.route("/post", methods=['GET', 'POST'])
def post():
    
    image   = request.form["image_link"]
    artist  = request.form["artist"]
    song    = request.form["song"]
    cap     = request.form["caption"]
    song_lookup = (artist + "%20" + song).replace(" ", "%20")
    # print(song_lookup)
    
    BASE_URL = 'https://api.spotify.com/v1/search?q={}&type=artist%2Ctrack&market=US&limit=10&offset=0'.format(song_lookup) # Create catch error for nothing found
    # print(BASE_URL)
    response    = requests.get(BASE_URL, headers=headers)
    data        = response.json()
    url         = data['tracks']['items'][0]['external_urls']['spotify']
    artist_name = data['tracks']['items'][0]['artists'][0]['name']
    track       = data['tracks']['items'][0]['name']
    preview     = data['tracks']['items'][0]['preview_url']
    if preview == None:
        preview = 'https://p.scdn.co/mp3-preview/b6f62ea05880c8fb58ff61f4d14a69a8a2f0cd73?cid=0a1cc09ac24240588678a1a1f217f200'
    album       = data['tracks']['items'][0]['album']['images'][0]['url']
    print(preview)
    GENIUS_token = os.environ['GENIUS_ACCESS']
    GENIUS_URL   = 'https://api.genius.com'
    
    song_lookup = (artist_name + "-" + track).replace(" ", "-")
    # print(song_lookup)
    
    path = 'search/'
    request_uri = '/'.join([GENIUS_URL, path])
    # print(request_uri + song_lookup)
    
    params   = {'q': song_lookup}
    
    token    = 'Bearer {}'.format(GENIUS_token)
    headers2 = {'Authorization': token}
    
    response = requests.get(request_uri, params=params, headers=headers2)
    data = response.json()
    # print(data)
    # print(data['response']['hits'][0]['result']['url'])
    try:
        lyrics_url = data['response']['hits'][0]['result']['url']
    except IndexError:
        lyrics_url = 'https://genius.com/search?q=does%20not%20exist'
    db.addPost(username, track, artist_name, preview, image, cap, lyrics_url)
    
    return flask.render_template("post.html",
                    song        = track,
                    name        = artist_name,
                    song_preview = preview,
                    album_image = album,
                    lyrics      = lyrics_url,
                    image_url   = image,
                    user        = username,
                    caption     = cap
                )
                


@app.route("/add_comment", methods=['GET', 'POST'])   
def add_comment():
    sender  = username;
    post_id = request.form["post_id"];
    message = request.form["message"];

    post_id     = request.form["post_id"]
    post_info   = db.getPostInfo(post_id);
    username1   = post_info[1]
    track       = post_info[2]
    artist_name = post_info[3]
    preview     = post_info[4]
    image       = post_info[5]
    cap         = post_info[6]
    lyrics_link = post_info[8]

    comments1 = []
    commenters1 = []
    
    db.addComment(sender, post_id, message);
    com_id_arr = db.getComments(post_id)
    
    for com_id in com_id_arr:
        comments1.append(db.getText('c', com_id))
        commenters1.append(db.getCreator('c', com_id))
        
    return flask.render_template("view_post.html",
        song        = track,
        name        = artist_name,
        song_preview = preview,
        image_url   = image,
        user        = username1,
        caption     = cap,
        comments    = comments1,
        commenters  = commenters1,
        post_id     = post_id,
        lyrics      = lyrics_link
    )            
                

                
@app.route("/view_post", methods=['GET', 'POST'])
def view_post():
    
    post_id     = request.form["post_id"]
    
    post_info   = db.getPostInfo(post_id);
    username1   = post_info[1]
    track       = post_info[2]
    artist_name = post_info[3]
    preview     = post_info[4]
    image       = post_info[5]
    cap         = post_info[6]
    lyrics_link = post_info[8]

    comms = db.getComments(post_id) #returns an array of comment_ids
    
    comments1 = []
    commenters1 = []
    for comm in comms:
        comments1.append(db.getText('c', comm))
        commenters1.append(db.getCreator('c', comm))
    
    return flask.render_template("view_post.html",
                    song        = track,
                    name        = artist_name,
                    song_preview = preview,
                    image_url   = image,
                    user        = username1,
                    caption     = cap,
                    comments    = comments1,
                    commenters  = commenters1,
                    post_id     = post_id,
                    lyrics      = lyrics_link
                )

@app.route("/user_page", methods=['GET', 'POST'])
def page():
    global username
    post_images=[]
    post_ids = db.getPosts(username)
                
    if len(post_ids) != 0:
        # print(post_ids)
        for post in post_ids:
            post_images.append(db.getImageLink(post))
        # print(post_images)
    else:
        post_ids = None
        post_images = None
    return flask.render_template("user.html", 
        user = username,
        ids = post_ids,
        snaps = post_images
    )
    
@app.route("/admin_page", methods=['GET', 'POST'])
def admin_page():
    username = request.form['current_user']
    post_images=[]
    post_ids = db.getPosts(username)
                
    if len(post_ids) != 0:
        # print(post_ids)
        for post in post_ids:
            post_images.append(db.getImageLink(post))
        # print(post_images)
    else:
        post_ids = None
        post_images = None
    return flask.render_template("admin.html", 
        user = username,
        ids = post_ids,
        snaps = post_images
    )

@app.route("/result", methods=['GET', 'POST'])
def result():
    # artists         = ["Gorillaz", "De Staat", "Steely Dan"]
    # artists_ID      = ["3AA28KZvwAUcZuOKwyblJQ", "4rZJKub3qA5t1yYcT3qmm4", "6P7H3ai06vU1sGvdpBwDmE"]
    # num1            = random.randint(0, 2)
    # num2            = random.randint(0,9)
    # rand_artist     = artists[num1]
    # rand_artist_ID  = artists_ID[num1]
    
    # # base URL of all Spotify API endpoints
    # BASE_URL = 'https://api.spotify.com/v1/artists/{}/top-tracks?market=US'.format(rand_artist_ID)
    # # print(BASE_URL)
        
    # # actual GET request with proper header
    # # song name, song artist, song-related image, song preview URL
    # response = requests.get(BASE_URL, headers=headers)
    # data     = response.json()
    # # print(data)
    # song_link   = data['tracks'][num2]['id']
    # song_name   = data['tracks'][num2]['name']
    # artist_name = data['tracks'][num2]['artists'][0]['name']
    # preview     = data['tracks'][num2]['preview_url']
    # song_image  = data['tracks'][num2]['album']['images'][0]['url']
    
    # BASE_URL     = 'https://api.spotify.com/v1/artists/{}'.format(rand_artist_ID)
    # response     = requests.get(BASE_URL, headers=headers)
    # data         = response.json()
    # artist_image = data['images'][0]['url']
    
    # GENIUS_token = os.environ['GENIUS_ACCESS']
    # GENIUS_URL   = 'https://api.genius.com'
    
    # song_lookup = (artist_name + "-" + song_name).replace(" ", "-")
    # # print(song_lookup)
    
    # path = 'search/'
    # request_uri = '/'.join([GENIUS_URL, path])
    # # print(request_uri + song_lookup)
    
    # params = {'q': song_lookup}
    
    # token    = 'Bearer {}'.format(GENIUS_token)
    # headers2 = {'Authorization': token}
    
    # response = requests.get(request_uri, params=params, headers=headers2)
    # data     = response.json()
    # # print(data)
    # # print(data['response']['hits'][0]['result']['url'])
    # lyrics_url = data['response']['hits'][0]['result']['url']
    
    global username
    username = request.form["username"]
    password = request.form["password"]
    post_images=[]
    if db.usernameTaken(username):
        if db.getPassword(username) == password:
            if db.getBlockStatus(username) == 1:
                return flask.render_template("user_disabled.html")
            else:
                if db.getAdminStatus(username) == 0: # If login is user
                    
                    post_ids = db.getPosts(username)
                    
                    if len(post_ids) != 0:
                        # print(post_ids)
                        for post in post_ids:
                            post_images.append(db.getImageLink(post))
                        # print(post_images)
                    else:
                        post_ids = None
                        post_images = None
                    return flask.render_template("user.html", 
                        user = username,
                        ids = post_ids,
                        snaps = post_images
                    )
                elif db.getAdminStatus(username) == 1: # If login is admin
                    post_ids = db.getPosts(username)
                    
                    if len(post_ids) != 0:
                        # print(post_ids)
                        for post in post_ids:
                            post_images.append(db.getImageLink(post))
                        # print(post_images)
                    else:
                        post_ids = None
                        post_images = None
                        
                    return flask.render_template("admin.html", 
                        user = username,
                        ids = post_ids,
                        snaps = post_images
                    )
        else: # If login is invalid
            return flask.render_template("attempt.html")
    else: # If login is invalid
        return flask.render_template("attempt.html")
        
        
@app.route("/admin_register", methods=['GET', 'POST'])
def admin_register():
        username = request.form['current_user']
        return flask.render_template("admin_register.html",
        user = username)

@app.route("/admin_create", methods=['GET', 'POST'])
def admin_create():
    username = request.form['username']
    create_username = request.form["create_username"]
    password = request.form["password"]
    try:
        admin_stat = request.form['admin_stat']
    except KeyError:
        admin_stat = 0
    
    if admin_stat == 0: # Create user
        db.addUser('NULL', 'NULL', create_username, password, 'NULL', 0)
    else: # Create admin
        db.addUser('NULL', 'NULL', create_username, password, 'NULL', 1)
    
    post_images=[]
    post_ids = db.getPosts(username)
                    
    if len(post_ids) != 0:
        # print(post_ids)
        for post in post_ids:
            post_images.append(db.getImageLink(post))
        # print(post_images)
    else:
        post_ids = None
        post_images = None
        
    return flask.render_template("admin.html", 
        user = username,
        ids = post_ids,
        snaps = post_images
    )

@app.route("/disable", methods=['GET', 'POST'])
def disable_function():
    username = request.form['current_user']
    return render_template("disable.html",
        user = username
        );
        
@app.route("/disable_confirmation", methods=['GET', 'POST'])
def disable_confirmation():
    username = request.form['current_user']
    selected_user   = request.form["selected_user"]
    db.setBlockStatus(selected_user, 1)
    return render_template("disable_confirmation.html",
            selected_user = selected_user,
            user = username
            );


@app.route("/register_admin", methods=['GET', 'POST'])
def register_admin():
        return render_template("register_admin.html"
        );

@app.route("/community", methods=['GET', 'POST'])
def community():
        return render_template("community.html"
        );

@app.route("/chat_list", methods=['GET', 'POST'])
def list_chats():
    user1   = request.form["current_user"]; 
    
    convo_arr = db.getConvos(user1);
    chat_users = [];
     #creates an array of usernames that the user has conversations with already
    for tup in convo_arr:              #tup = (user1, user2)
        if tup[0] == user1:
            chat_users.append(tup[1]);
        else:
            chat_users.append(tup[0]);
    
    return render_template("chat_list.html",
            user1       = user1,
            chat_users  = chat_users
            );
    


@app.route("/new_chat", methods=['GET', 'POST']) 
def create_chat():
    
    user1   = request.form["current_user"]; 
    user2   = request.form["searched_user"];
    convo_id = db.getConvoId(user1, user2)
    message_arr   = [];
    
    if convo_id == -1:
        db.addConvo(user1, user2);
        '''
        convo_id = db.getConvoId(user1, user2);
        dictionary = {
            "user1" : user1,
            "user2" : user2,
            "convo_id" : convo_id
            }
        json_var = json.dumps(dictionary);
        
        socketio.emit("chat_added", json_var);
        '''
    else: # I know this is duplicated code from view_chat(). I just want this to work right now
        message_tuples = db.getMessageTuples(convo_id);
        #initializes return array           
        #tuples(msg_id, convo_id, sender, receiver, message, mtime, is_read)
        for tup in message_tuples:
            message_arr.append( str(tup[2])+" : "+str(tup[4]) );
    
    return render_template("chat.html",
            convo_id    = convo_id,
            user1       = user1,
            user2       = user2,
            message_arr = message_arr
            );
        


@app.route("/chat", methods=['GET', 'POST'])
def view_chat():
    
    user1       = request.form["user1"];
    user2       = request.form["user2"];
    convo_id    = db.getConvoId(user1, user2);
    message_tuples = db.getMessageTuples(convo_id);
    message_arr   = [];
    
    #initializes return array           
    #tuples(msg_id, convo_id, sender, receiver, message, mtime, is_read)
    for tup in message_tuples:
        message_arr.append( str(tup[2])+" : "+str(tup[4]) );
    
    
    return render_template("chat.html",
            convo_id    = convo_id,
            user1       = user1,
            user2       = user2,
            message_arr = message_arr
            );
    
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')
  

@socketio.on('message')
def on_message(json, methods=['GET', 'POST']):

    #add message to database
    db.addMessage(json["convo_id"], json["sender"], json["receiver"], json["message"] );

    print('received my event: ' + str(json))
    socketio.emit('response', json, callback=messageReceived)

    


socketio.run(
    app,
    host=os.getenv("IP", "0.0.0.0"), 
    port=int(os.getenv("PORT", 8080)), 
    debug=True
)


