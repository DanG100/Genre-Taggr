
# shows a user's playlists (need to be authenticated via oauth)

from __future__ import print_function
import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
from mutagen.easyid3 import EasyID3

client_id = ''
client_secret = ''

def writeGenre(sp,track,path):
    try:
        audio = EasyID3(path)
        audio['catalognumber'] = track['uri']
        if audio.get('genre', "") == "":
            artist = sp.artist(track['artists'][0]['id'])
            if artist['genres']:
                print(artist['genres'])
                audio['genre'] = ', '.join(artist['genres'])
                audio['catalognumber'] = track['uri']
        audio.save()
    except:
        print("failed to get artist info")


def findTrack(sp,path):
    song = EasyID3(path)
    id3_artist = song['artist'][0]
    id3_title = song['title'][0]
    if song.get('genre', "") == "":
        results = sp.search(q=id3_artist + ' ' + id3_title, type='track')
        tracks = results['tracks']['items']
        for track in tracks:
            spot_title = track['name']
            spot_artist = track['artists'][0]['name']
            if id3_title == spot_title and id3_artist == spot_artist:
                print("Found match")
                writeGenre(sp,track,path)
                break
            else:
                print("ID3 Artist: " + id3_artist + ", Spotify Artist: " + spot_artist)
                print("ID3 Title: " + id3_title + ", Spotify Title: " + spot_title)
    else:
        print("Skipping track, already has genre info")


if __name__ == '__main__':
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    cwd = os.getcwd()
    # print(EasyID3.valid_keys.keys())
    for folder, subdirs, files in os.walk(cwd):
        for filename in files:
            path = os.path.join(folder, filename)
            if path.endswith('.mp3'):
                findTrack(sp,path)



