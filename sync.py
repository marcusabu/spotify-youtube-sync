from spotify import Spotify
from youtube import Youtube

spotify_client_ID = 'YOUR SPOTIFY CLIENT ID'
spotify_client_secret = 'YOUR SPOTIFY CLIENT SECRET'
spotify_username = 'YOUR SPOTIFY USERNAME'
spotify_playlist_id = 'YOUR SPOTIFY PLAYLIST ID'

youtube_playlist_id = "YOUR YOUTUBE PLAYLIST ID"

spotify = Spotify(spotify_username,
                  spotify_playlist_id, spotify_client_ID,
                  spotify_client_secret)
youtube = Youtube(youtube_playlist_id)
youtube.get_video_list()

print "\nSyncing every Spotify track with the playlist..."
for track in spotify.tracks:
    youtube.sync_with_playlist(track)

print "\nCompleted sync, exiting\n\n"
