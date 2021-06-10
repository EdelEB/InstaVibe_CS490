import requests
import os
import flask
from flask import request
from dotenv import load_dotenv, find_dotenv
import random
import database.db_func as db
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

print('Link to song: https://open.spotify.com/track/{}'.format(song_link))
print('Song Name: {}'.format(song_name))
print('By: {}'.format(artist_name))
print('Preview: {}'.format(preview))
print('Song Image: {}'.format(song_image))

BASE_URL = 'https://api.spotify.com/v1/artists/{}'.format(rand_artist_ID)
response = requests.get(BASE_URL, headers=headers)
data = response.json()
artist_image = data['images'][0]['url']

song_lookup = (artist_name + "%20" + song_name).replace(" ", "%20")
# print(song_lookup)

BASE_URL = 'https://api.spotify.com/v1/search?q={}&type=artist%2Ctrack&market=US&limit=10&offset=0'.format(song_lookup)
print(BASE_URL)
response = requests.get(BASE_URL, headers=headers)
data = response.json()
#print(data)
print("\n\n")
#print(data['tracks']['items'][0]['external_urls']['spotify'])
print(data['tracks']['items'][0])
print(data['tracks']['items'][0]['album']['images'][0]['url'])

#print(data['tracks']['items'][0]['artists'][0]['name'])
#print(data['tracks']['items'][0]['name'])
#print(data['tracks']['items'][0]['preview_url'])
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