import sys

import requests

import random

if len(sys.argv) < 2:
    sys.exit('Please enter something!')
res = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

data = res.json()

song_list = data['results']

if song_list:
    random_song = random.choice(song_list)
    print(f"Recommended song by {sys.argv[1]}: {random_song['trackName']} 🎶")



    
