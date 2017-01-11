import spotipy
import spotipy.util as util
import json

class Spotify:

    def __init__(self, username, playlist_id, client_id, client_secret):
        self.tracks = []

        auth = spotipy.oauth2.SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret)
        token = auth.get_access_token()

        sp = spotipy.Spotify(auth=token)
        results = sp.user_playlist_tracks(username, playlist_id)
        for item in results['items']:
            self.tracks.append("{} - {}".format(
                item[u'track'][u'artists'][0][u'name'],
                item[u'track'][u'name']
            ))
        while results['next']:
            results = sp.next(results)
            for item in results['items']:
                self.tracks.append("{} - {}".format(
                    item['track']['artists'][0]['name'].encode('utf-8'),
                    item['track']['name'].encode('utf-8')
                ))

        print "Retrieved Spotify information."
