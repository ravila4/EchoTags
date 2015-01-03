#!/usr/bin/python3
# project         :EchoTags
# title           :echotag.py
# description     :Program for tagging mp3 files with various useful attributes.
# author          :ravila
# date            :January 02, 2015
# version         :
# usage           :python3 track_upload.py path-audio audio-type
# notes           :
# python_version  :3.4
# ==============================================================================
# To Do:
#  - handle multiple files with wildcards
#  - support for other file types
#
# ===============================================================================


import pyen
import sys
import time
from mutagen.id3 import ID3, TXXX

en = pyen.Pyen('D6JNAFBHJO6UD84Z7')
en.trace = False


def wait_for_analysis(id):
    print('Fetching track attributes...')
    time.sleep(1)
    while True:
        # Make an API call for track's audio_summary and retry every second until complete.
        response = en.get('track/profile', id=id, bucket=['audio_summary'])
        if response['track']['status'] != 'pending':
            break
        time.sleep(1)
    print('\n')
    # Print audio_summary attributes
    for k, v in response['track']['audio_summary'].items():
        print("%s: %s" % (k, str(v)))
        # Save attributes to tags
        audio.add(TXXX(encoding=0, desc=k, text=str(v)))
        audio.save()
    print('\n Complete. All attributes saved to tags.')

if len(sys.argv) > 2:
    # Initial parameters
    mp3 = sys.argv[1]
    type = sys.argv[2]

    # Open file and initiate ID3 tagging method
    f = open(mp3, 'rb')
    audio = ID3(mp3)
    # Check if track_id exists in tags
    if audio.get('TXXX:TRACK_ID') is None:
        # Tag doesn't exist. Upload file and obtain ID
        print('Fetching track ID...')
        response = en.post('track/upload', track=f, filetype=type)
        trid = response['track']['id']
        print('Track id is', trid)

        # Saving ID tag to file
        audio.add(TXXX(encoding=0, desc='TRACK_ID', text=trid))
        audio.save()
        print('\n')
        print('ID saved to tag: track_id = ', audio.get('TXXX:TRACK_ID'))

    else:
        # Tag exists, obtain value.
        trid = audio.get('TXXX:TRACK_ID')
        print('Track id is', trid)

    # Call function to analyze track's acoustic properties
    wait_for_analysis(trid)

else:
    # Error message if wrong number of parameters are passed.
    print("usage: python3 track_upload.py path-audio audio-type")