# Genre-Taggr

This script tries to find and write to the ID3 tag the song's genre, using Spotify API. It recurvisely scans the cwd for every mp3 file to identify the genre.

### Install Dependencies

* Install python and pip
* (Recommended) Add python to PATH variable, or equivalent for Mac and Linux
```
pip install mutagen
pip install spotipy
```

### Usage

[Download](https://github.com/DanG100/Genre-Taggr/releases/latest) script and place in top level of music directory. Fill in client id and client secret from the [Spotify Developer](https://developer.spotify.com/my-applications/) page. Run script.

```
python genre_tagger.py
```
