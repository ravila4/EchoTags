#!/usr/bin/python3
# project         :EchoTags
# title           :echotest.py
# description     :Testing various calls to the Echonest API
# author          :ravila
# date            :January 02, 2015
# version         :
# usage           :
# notes           :
# python_version  :3.4
# ==============================================================================

import pyen
import logging

logging.getLogger('pyen').setLevel(logging.DEBUG)

en = pyen.Pyen('D6JNAFBHJO6UD84Z7')

# Create a list of similar artists
print('===============================================')
response = en.get('artist/similar', name='weezer')
for artist in response['artists']:
    print(artist['id'], artist['name'])

# Create a static artist-based playlist
print('===============================================')
response = en.get('playlist/static', artist='amanda palmer', type='artist-radio')
for i, song in enumerate(response['songs']):
    print("%d %-32.32s %s" % (i, song['artist_name'], song['title']))

# Search for songs in the Echonest database and return their ID.
print('===============================================')
response = en.get('song/search', artist='amanda palmer', title='the killing type')
for song in response['songs']:
    print("%s - %s %32.32s" % (song["artist_name"], song["title"], song["id"]))

# Get track attributes by ID
print('===============================================')
response = en.get('track/profile', id='TRTLKZV12E5AC92E11', format='json', bucket='audio_summary')
track = response['track']
audio_summary = track['audio_summary']

print("TRACK: %s by %s\n" % (track['title'], track['artist']))
print("mode:", audio_summary['mode'])
print("key:", audio_summary['key'])
print("tempo:", audio_summary['tempo'])
print("time_signature:", audio_summary['time_signature'])
print("loudness:", audio_summary['loudness'])
print("valence:", audio_summary['valence'])
print("energy:", audio_summary['tempo'])
print("acousticness:", audio_summary['acousticness'])
print("danceability:", audio_summary['danceability'])
print("speechiness:", audio_summary['speechiness'])
print("ID:", track['id'])
print("song_ID:", track['song_id'])