#youtube new music

import requests
from bs4 import BeautifulSoup
import re
import csv


key=API_KEY('xAIzaSyBon_xxNw-xybyh7gYwguhKTkfVVM4e7CI')

allsongs = []
youtubebaseurl = requests.get('https://www.youtube.com/playlist?list=PL2BBFi7UvppsE_8WDMYRa9zFoh2LlET3Z')
youtubebs = BeautifulSoup(youtubebaseurl.text, 'lxml')

songtiles = youtubebs.find_all('ytd-playlist-video-renderer', attrs = {'class':'ytd-playlist-video'} )

for song in songtiles:
    singlesong={}
    songName = song.find('h3', attrs = {'class':'ytd-playlist-video-renderer'})

    singlesong[songName] = songName.find().text.encode('utf-8')
    allsongs.append(singlesong)

print(allsongs)
print(youtubebs)

# API stuff
