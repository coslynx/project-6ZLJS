import soundcloud
from soundcloud.resource import Resource
import requests

class SoundCloudAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client = soundcloud.Client(client_id=self.client_id, client_secret=self.client_secret)

    def search_track(self, query):
        """Searches for a track on SoundCloud."""
        try:
            tracks = self.client.get('/tracks', q=query)
            return tracks
        except Exception as e:
            print(f"Error searching for track on SoundCloud: {e}")
            return None

    def get_track_info(self, track_url):
        """Retrieves detailed information about a track."""
        try:
            track = self.client.get('/resolve', url=track_url)
            return track
        except Exception as e:
            print(f"Error retrieving track information from SoundCloud: {e}")
            return None

    def get_playlist_tracks(self, playlist_url):
        """Retrieves tracks from a SoundCloud playlist."""
        try:
            playlist = self.client.get('/resolve', url=playlist_url)
            tracks = playlist.tracks
            return tracks
        except Exception as e:
            print(f"Error retrieving tracks from SoundCloud playlist: {e}")
            return None

    def get_user_playlists(self, user_id):
        """Retrieves playlists belonging to a user."""
        try:
            playlists = self.client.get(f'/users/{user_id}/playlists')
            return playlists
        except Exception as e:
            print(f"Error retrieving playlists from SoundCloud user: {e}")
            return None

    def get_track_audio_url(self, track_url):
        """Retrieves the audio URL for a SoundCloud track."""
        try:
            track = self.client.get('/resolve', url=track_url)
            audio_url = track.stream_url
            return audio_url
        except Exception as e:
            print(f"Error retrieving audio URL for SoundCloud track: {e}")
            return None