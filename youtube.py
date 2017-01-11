import httplib2
import os
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


class Youtube:

    def __init__(self, playlist_id):
        self.videos = []
        self.playlist_id = playlist_id

        client_secrets_file = "client_secrets.json"
        youtube_scope = "https://www.googleapis.com/auth/youtube"
        youtube_api_service_name = "youtube"
        youtube_api_version = "v3"

        flow = flow_from_clientsecrets(client_secrets_file, scope=youtube_scope, message='client_secrets.json not found.')
        storage = Storage("%s-oauth2.json" % sys.argv[0])
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = run_flow(flow, storage)
        self.youtube = build(youtube_api_service_name, youtube_api_version,http=credentials.authorize(httplib2.Http()))

    def sync_with_playlist(self, track):
        artist = track.split('-')[0]
        title = track.split('-')[1]
        for video in self.videos:
            if artist.lower() in video['title'].lower() and title.lower() in video['title'].lower():
                return
        video_id = self.get_video_id(track)
        for video in self.videos:
            if video_id == video['id']:
                return
        self.add_video_to_playlist(video_id)
        print "Added: {}-{}".format(artist, title)

    def get_video_id(self, keyword):
        get_video = self.youtube.search().list(
            q=keyword,
            part="id,snippet",
            maxResults=1
        ).execute()

        return get_video[u'items'][0][u'id'][u'videoId']

    def get_video_list(self):
        get_videos_request = self.youtube.playlistItems().list(
            part="snippet",
            playlistId=self.playlist_id,
            maxResults=50
        ).execute()

        for item in get_videos_request['items']:
            self.videos.append({
                'title': item[u'snippet'][u'title'].encode('utf-8'),
                'id': item[u'snippet'][u'resourceId'][u'videoId'].encode('utf-8')
            })

        while 'nextPageToken' in get_videos_request:
            get_videos_request = self.youtube.playlistItems().list(
                part="snippet",
                playlistId=self.playlist_id,
                maxResults=50,
                pageToken=get_videos_request['nextPageToken']
            ).execute()

            for item in get_videos_request['items']:
                self.videos.append({
                    'title': item[u'snippet'][u'title'].encode('utf-8'),
                    'id': item[u'snippet'][u'resourceId'][u'videoId'].encode('utf-8')
                })

        print "Retireved Youtube information."

    def add_video_to_playlist(self, video_id):
        add_video_request = self.youtube.playlistItems().insert(
            part="snippet",
            body={
                'snippet': {
                    'playlistId': self.playlist_id,
                    'resourceId': {
                        'kind': 'youtube#video',
                        'videoId': video_id
                    }
                    # 'position': 0
                }
            }
        ).execute()