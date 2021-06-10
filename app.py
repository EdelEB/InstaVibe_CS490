import requests
import os
import flask
from flask import request
from dotenv import load_dotenv, find_dotenv
import random
import database.db_func as db


app=flask.Flask(__name__)

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
    image = request.form["image_link"]
    artist = request.form["artist"]
    song = request.form["song"]
    cap = request.form["caption"]
    song_lookup = (artist + "%20" + song).replace(" ", "%20")
    # print(song_lookup)
    
    BASE_URL = 'https://api.spotify.com/v1/search?q={}&type=artist%2Ctrack&market=US&limit=10&offset=0'.format(song_lookup) # Create catch error for nothing found
    # print(BASE_URL)
    response = requests.get(BASE_URL, headers=headers)
    data = response.json()
    url = data['tracks']['items'][0]['external_urls']['spotify']
    artist_name = data['tracks']['items'][0]['artists'][0]['name']
    track = data['tracks']['items'][0]['name']
    preview = data['tracks']['items'][0]['preview_url']
    album = data['tracks']['items'][0]['album']['images'][0]['url']
    
    GENIUS_token = os.environ['GENIUS_ACCESS']
    GENIUS_URL = 'https://api.genius.com'
    
    song_lookup = (artist_name + "-" + track).replace(" ", "-")
    # print(song_lookup)
    
    path = 'search/'
    request_uri = '/'.join([GENIUS_URL, path])
    # print(request_uri + song_lookup)
    
    params = {'q': song_lookup}
    
    token = 'Bearer {}'.format(GENIUS_token)
    headers2 = {'Authorization': token}
    
    response = requests.get(request_uri, params=params, headers=headers2)
    data = response.json()
    # print(data)
    # print(data['response']['hits'][0]['result']['url'])
    lyrics_url = data['response']['hits'][0]['result']['url']
    db.addPost(username, track, artist_name, preview, image, cap)
    
    return flask.render_template("post.html",
                    song = track,
                    name = artist_name,
                    song_preview = preview,
                    album_image = album,
                    song_lyrics = lyrics_url,
                    image_url = image,
                    user = username,
                    caption = cap
                )
                
                
@app.route("/view_post", methods=['GET', 'POST'])
def view_post():
    post_id = request.form[num]
    post_info = db.__getPostInfo(post_id)
    username = post_info[1]
    track = post_info[2]
    artist_name = post_info[3]
    preview = post_info[4]
    image = post_info[5]
    cap = post_info(6)
    
    return flask.render_template("view_post.html",
                    song = track,
                    name = artist_name,
                    song_preview = preview,
                    image_url = image,
                    user = username,
                    caption = cap
                )

@app.route("/result", methods=['GET', 'POST'])
def result():
    artists = ["Gorillaz", "De Staat", "Steely Dan"]
    artists_ID = ["3AA28KZvwAUcZuOKwyblJQ", "4rZJKub3qA5t1yYcT3qmm4", "6P7H3ai06vU1sGvdpBwDmE"]
    num1 = random.randint(0, 2)
    num2 = random.randint(0,9)
    rand_artist = artists[num1]
    rand_artist_ID = artists_ID[num1]
    
    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/artists/{}/top-tracks?market=US'.format(rand_artist_ID)
    # print(BASE_URL)
        
    
    # actual GET request with proper header
    # song name, song artist, song-related image, song preview URL
    response = requests.get(BASE_URL, headers=headers)
    data = response.json()
    # print(data)
    song_link = data['tracks'][num2]['id']
    song_name = data['tracks'][num2]['name']
    artist_name = data['tracks'][num2]['artists'][0]['name']
    preview = data['tracks'][num2]['preview_url']
    song_image = data['tracks'][num2]['album']['images'][0]['url']
    
    # print('Link to song: https://open.spotify.com/track/{}'.format(song_link)
    # print('Song Name: {}'.format(song_name))
    # print('By: {}'.format(artist_name)_
    # print('Preview: {}'.format(preview)_
    # print('Song Image: {}'.format(song_image))
    
    BASE_URL = 'https://api.spotify.com/v1/artists/{}'.format(rand_artist_ID)
    response = requests.get(BASE_URL, headers=headers)
    data = response.json()
    artist_image = data['images'][0]['url']
    
    GENIUS_token = os.environ['GENIUS_ACCESS']
    GENIUS_URL = 'https://api.genius.com'
    
    song_lookup = (artist_name + "-" + song_name).replace(" ", "-")
    # print(song_lookup)
    
    path = 'search/'
    request_uri = '/'.join([GENIUS_URL, path])
    # print(request_uri + song_lookup)
    
    params = {'q': song_lookup}
    
    token = 'Bearer {}'.format(GENIUS_token)
    headers2 = {'Authorization': token}
    
    response = requests.get(request_uri, params=params, headers=headers2)
    data = response.json()
    # print(data)
    # print(data['response']['hits'][0]['result']['url'])
    lyrics_url = data['response']['hits'][0]['result']['url']
    
    global username
    username = request.form["username"]
    password = request.form["password"]
    post_images=[]
    if db.usernameTaken(username):
        if db.getPassword(username) == password:
            if db.getAdminStatus(username) == 0: # If login is user
                post_ids = db.getPosts(username)
                if len(post_ids) != 0:
                    print(post_ids)
                    for post in post_ids:
                        post_images.append(db.getImageLink(post))
                    print(post_images)
                else:
                    post_ids = None
                    post_images = None
                return flask.render_template("user.html", 
                    song_url = song_link,
                    song = song_name,
                    name = artist_name,
                    song_preview = preview,
                    image_url = song_image,
                    artist_img = artist_image,
                    song_lyrics = lyrics_url,
                    user = username,
                    ids = post_ids,
                    snaps = post_images
                )
            elif db.getAdminStatus(username) == 1: # If login is admin
                return flask.render_template("admin.html", 
                    song_url = song_link,
                    song = song_name,
                    name = artist_name,
                    song_preview = preview,
                    image_url = song_image,
                    artist_img = artist_image,
                    song_lyrics = lyrics_url,
                    user = username
                )
        else: # If login is invalid
            return flask.render_template("attempt.html")
    else: # If login is invalid
        return flask.render_template("attempt.html")


app.run(
    port=int(os.getenv("PORT", 8080)), 
    host=os.getenv("IP", "0.0.0.0"), 
    debug=True)