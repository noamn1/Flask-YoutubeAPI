from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class YoutubeFetcher:


    # Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
    # tab of
    #   https://cloud.google.com/console
    # Please ensure that you have enabled the YouTube Data API for your project.
    DEVELOPER_KEY = '%DEVELOPER_KEY%'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    def youtube_search(self, q, max_results):
        youtube = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION,
                        developerKey=self.DEVELOPER_KEY)

        # Call the search.list method to retrieve results matching the specified
        # query term.
        search_response = youtube.search().list(
            q=q,
            part='id,snippet',
            maxResults=max_results
        ).execute()

        videos = []
        channels = []
        playlists = []

        # Add each result to the appropriate list, and then display the lists of
        # matching videos, channels, and playlists.
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append('%s (%s)' % (search_result['snippet']['title'],
                                           search_result['id']['videoId']))
            elif search_result['id']['kind'] == 'youtube#channel':
                channels.append('%s (%s)' % (search_result['snippet']['title'],
                                             search_result['id']['channelId']))
            elif search_result['id']['kind'] == 'youtube#playlist':
                playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                              search_result['id']['playlistId']))

        print('Videos:\n', '\n'.join(videos))
        print('Channels:\n', '\n'.join(channels))
        print('Playlists:\n', '\n'.join(playlists))

        return [videos, channels, playlists]

    def __init__(self):
        pass
