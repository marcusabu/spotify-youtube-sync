# spotify-youtube-sync
This script looks at every track in a given Spotify playlist. If the track in not in the Youtube playlist, it inserts the video in it.

## Prerequisites
1. A Spotify developer application (https://developer.spotify.com/my-applications/#!/applications)
2. client_secrets.json containing Youtube Data API credentials
3. The ID of the desired Spotify playlist
4. The ID of the desired Youtube playlist

## Setup
Insert your credentials in sync.py
~~~
spotify_client_ID = 'YOUR SPOTIFY CLIENT ID'
spotify_client_secret = 'YOUR SPOTIFY CLIENT SECRET'
spotify_username = 'YOUR SPOTIFY USERNAME'
spotify_playlist_id = 'YOUR SPOTIFY PLAYLIST ID'
youtube_playlist_id = 'YOUR YOUTUBE PLAYLIST ID'
~~~

## Running
~~~
python sync.py
~~~

## TODO
Obviously, this script is in an early development stage. Things to do:
  1. Delete videos from playlist
  2. Command line arguments for playlists
  3. PEP8
  4. Python 3 support

## Contact
For questions: marcusabu@gmail.com
