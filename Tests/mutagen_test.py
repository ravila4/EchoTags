#!/usr/bin/python3
# project         :EchoTags
# title           :test2.py
# description     :Tests related to ID3 tag saving and opening.
# author          :ravila
# date            :January 02, 2015
# version         :
# usage           :
# notes           :
# python_version  :3.4
# ==============================================================================

from mutagen.id3 import ID3, TXXX, TPE1, ID3NoHeaderError

# Open file
# This method prevents an 'ID3NoHeader' error if the track has no tags.
try:
    audio = ID3('example.mp3')
except ID3NoHeaderError:
    audio = ID3()
    audio.add(TPE1(encoding=3, text=u'Artist'))
    audio.save('example.mp3')

# Writing a custom TXX tag with the ID3 module.
audio.add(TXXX(encoding=0, desc='TRACK_ID', text=['TRQNFKP14AAEDDC9D7']))
audio.save()
print('Track ID:', audio.get('TXXX:TRACK_ID'))

# Obtaining title, album and artist tags.
artist = audio.get('TPE1')
title = audio.get('TIT2')
album = audio.get('TALB')
print('Artist: ', artist)
print('Ttitle: ', title)
print('Album: ', album)

