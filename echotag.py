#!/usr/bin/python3
# project         :EchoTags
# title           :echotag.py
# description     :Program for tagging mp3 files with various useful attributes.
# author          :ravila4
# date            :January 06, 2015
# version         :2.0
# usage           :python3 track_upload.py path-audio
# notes           :Multiple audi files may be opened using a wildcard. Like so: *.mp3
# python_version  :3.4
# ==============================================================================
# TODO: Add support for other file types.
# TODO: Issue a warning when the file is not found in database.


import sys
import os
import pyen
from mutagen.id3 import ID3, TXXX
from termcolor import colored


# Set an environment variable: 'ECHO_NEST_API_KEY'
key = os.environ.get('ECHO_NEST_API_KEY')
en = pyen.Pyen(key)  # Alternatively, enter your API key here.


def get_attributes(a, t):
    # Search for song in Echo Nest database
    response = en.get('song/search', artist=a, title=t, results=1, bucket='audio_summary')
    # If a song is found, save attributes to tags.
    for song in response['songs']:
        song_id = song['id']
        audio.add(TXXX(encoding=0, desc='SONG_ID', text=song_id))
        for k, v in song['audio_summary'].items():
            audio.add(TXXX(encoding=0, desc=k, text=str(v)))
        audio.save()
        print(colored('All attributes saved to tags.', 'green'))


if len(sys.argv) > 1:
    x = len(sys.argv) - 1  # Number of files opened

    for f in range(1, x):
        # Open audio files one at a time
        file = sys.argv[f]
        audio = ID3(file)
        # Read ID3 tags
        artist = audio.get('TPE1')
        title = audio.get('TIT2')
        print('\nOpened file:', os.path.basename(file))

        # Exclude files if missing artist or title tags and output a red warning message.
        if artist is None:
            if title is None:
                print(colored('Artist and title tags missing, skipping track...', 'red'))
            else:
                print(colored('Artist tag missing, skipping track...', 'red'))

        elif title is None:
            print(colored('Title tag missing, skipping track...', 'red'))

        else:
            # File has both artist and title tags.
            print('%s by %s' % (title, artist))
            get_attributes(artist, title)


else:

    # Error message if wrong number of parameters are passed.
    print("usage: python3 track_upload.py path-audio")