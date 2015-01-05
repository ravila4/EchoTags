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

########################################################################
#  The following blocks of code are a list of miscellaneous API calls  #
########################################################################

import os
import pyen

# Set an environment variable: 'ECHO_NEST_API_KEY'
key = os.environ.get('ECHO_NEST_API_KEY')
en = pyen.Pyen(key)  # Alternatively, enter your API key here.

# Create a list of similar artists
print('===============================================')
print('A list of similar artists:\n')
response = en.get('artist/similar', name='weezer')
for artist in response['artists']:
    print(artist['id'], artist['name'])


# Create a static artist-based playlist
print('===============================================')
print('An artist based playlist:\n')
response = en.get('playlist/static', artist='amanda palmer', type='artist-radio')
for i, song in enumerate(response['songs']):
    print("%d %-32.32s %s" % (i, song['artist_name'], song['title']))


''' The Echo Nest provides several types of IDs that may be useful,
    song and artist IDs may be obtained by using the 'song/search'
    track IDs may be obtained using the track/upload methods. '''


# The example below gets a list of acoustic attributes attributes using the track ID.
# Track ID is obtained by uploading a file for analysis. However, this may be time consuming.

# Obtaining Track ID
print('========================================================================')
print('Uploading song for analysis...')
f = open('example.mp3', 'rb')
response = en.post('track/upload', track=f, filetype='mp3')
track_id = response['track']['id']
print("%s - %s    Track ID: %s\n" % (response['track']["artist"], response['track']["title"], track_id))

# Obtaining attributes
print('Acoustic Attributes from Track ID:\n')
response = en.get('track/profile', id=track_id, format='json', bucket='audio_summary')
# Printing the output
for k, v in response['track']['audio_summary'].items():
    print("%s: %s" % (k, str(v)))


# A faster way to get attributes is to obtain a song ID by passing an artist's name and song title.


# Obtaining song ID.
print('========================================================================')
response = en.get('song/search', artist='amanda palmer', title='the killing type', results=1)
for song in response['songs']:
    song_id = song['id']
    print("%s - %s    Song ID: %s\n" % (song["artist_name"], song["title"], song_id))


# Obtaining Attributes.
print('Acoustic Attributes from Song ID:\n')
response = en.get('song/profile', id=song_id, format='json', bucket='audio_summary')
# Printing the output
for song in response['songs']:  # I'm still not sure why it's different than the track method, but it works.
    for k, v in song['audio_summary'].items():
        print("%s: %s" % (k, str(v)))

# Or, even easier... do both of these things at once:
print('========================================================================')
print('Acoustic Attributes from song search:\n')
response = en.get('song/search', artist='amanda palmer', title='the killing type', results=1, bucket='audio_summary')
for song in response['songs']:
    for k, v in song['audio_summary'].items():
        print("%s: %s" % (k, str(v)))
