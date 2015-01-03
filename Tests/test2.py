#!/usr/bin/python3
# project         :EchoTags
# title           :test2.py
# description     :Testing mutagen tag saving.
# author          :ravila
# date            :January 02, 2015
# version         :
# usage           :
# notes           :
# python_version  :3.4
# ==============================================================================

from mutagen.id3 import ID3, TXXX


audio = ID3("example.mp3")
audio.add(TXXX(encoding=0, desc='TRACK_ID', text=['TRQNFKP14AAEDDC9D7']))
audio.save()
print(audio.get('TXXX:TRACK_ID'))
