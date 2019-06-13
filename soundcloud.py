#soundcloud new music

#seems like it needs to be javascript?
import requests
from bs4 import BeautifulSoup
import re
import csv


allsongs = []
soundcloudbaseurl = requests.get('https://soundcloud.com/you/likes')
soundcloudbs = BeautifulSoup(soundcloudbaseurl.text, 'lxml')

songtiles = soundcloudbs.find_all('li', attrs = {'class':'badgeList__item'} )

for song in songtiles:
    singlesong={}
    songName = song.find('a', attrs = {'class':'playableTile__mainHeading'})

    singlesong[songName] = songName.find().text.encode('utf-8')
    allsongs.append(singlesong)

print(allsongs)
print(soundcloudbs)
