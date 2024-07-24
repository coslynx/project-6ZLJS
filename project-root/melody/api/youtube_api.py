from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests

class YouTubeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def search_video(self, query):
        """Searches for a video on YouTube based on a query."""
        try:
            search_response = self.youtube.search().list(
                q=query,
                part='id,snippet',
                maxResults=1,
                type='video'
            ).execute()

            if search_response['items']:
                video_id = search_response['items'][0]['id']['videoId']
                return video_id
            else:
                return None

        except HttpError as e:
            print(f'Error searching for video on YouTube: {e}')
            return None

    def get_video_info(self, video_id):
        """Retrieves detailed information about a YouTube video."""
        try:
            video_response = self.youtube.videos().list(
                part='snippet,contentDetails',
                id=video_id
            ).execute()

            if video_response['items']:
                video_info = video_response['items'][0]
                return video_info
            else:
                return None

        except HttpError as e:
            print(f'Error retrieving video information from YouTube: {e}')
            return None

    def get_video_url(self, video_id):
        """Retrieves the URL of a YouTube video."""
        return f'https://www.youtube.com/watch?v={video_id}'