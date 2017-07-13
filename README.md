# Genre-Taggr

Tries to find and tag songs genre, using Spotify API. Recurvisely scans the cwd for every mp3 file to find match.

### Install Dependicies
  
```
pip install mutagen
pip install spotipy
```

### Usage

Download script and place in top level of music directory. Fill in client id and client secret from the [Spotify Developer](https://developer.spotify.com/my-applications/) page. Run script.

```
python genre_tagger.py
```
