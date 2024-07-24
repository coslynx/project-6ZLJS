import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)

    def search_track(self, query):
        """Searches for a track on Spotify based on a query."""
        try:
            results = self.sp.search(q=query, type='track', limit=1)
            if results['tracks']['items']:
                track_info = results['tracks']['items'][0]
                return track_info
            else:
                return None
        except Exception as e:
            print(f"Error searching for track on Spotify: {e}")
            return None

    def get_track_info(self, track_id):
        """Retrieves detailed information about a track."""
        try:
            track_info = self.sp.track(track_id)
            return track_info
        except Exception as e:
            print(f"Error retrieving track information from Spotify: {e}")
            return None

    def get_playlist_tracks(self, playlist_id):
        """Retrieves tracks from a Spotify playlist."""
        try:
            tracks = self.sp.playlist_tracks(playlist_id)
            return tracks['items']
        except Exception as e:
            print(f"Error retrieving tracks from Spotify playlist: {e}")
            return None

    def get_user_playlists(self, user_id):
        """Retrieves playlists belonging to a user."""
        try:
            playlists = self.sp.user_playlists(user_id)
            return playlists['items']
        except Exception as e:
            print(f"Error retrieving playlists from Spotify user: {e}")
            return None

    def get_track_audio_url(self, track_id):
        """Retrieves the audio URL for a Spotify track."""
        try:
            track_info = self.sp.track(track_id)
            audio_url = track_info['preview_url']
            return audio_url
        except Exception as e:
            print(f"Error retrieving audio URL for Spotify track: {e}")
            return None

    def get_artist_info(self, artist_id):
        """Retrieves detailed information about an artist."""
        try:
            artist_info = self.sp.artist(artist_id)
            return artist_info
        except Exception as e:
            print(f"Error retrieving artist information from Spotify: {e}")
            return None

    def get_artist_albums(self, artist_id):
        """Retrieves albums by an artist."""
        try:
            albums = self.sp.artist_albums(artist_id)
            return albums['items']
        except Exception as e:
            print(f"Error retrieving albums from Spotify artist: {e}")
            return None

    def get_album_tracks(self, album_id):
        """Retrieves tracks from an album."""
        try:
            tracks = self.sp.album_tracks(album_id)
            return tracks['items']
        except Exception as e:
            print(f"Error retrieving tracks from Spotify album: {e}")
            return None

    def get_related_artists(self, artist_id):
        """Retrieves related artists."""
        try:
            artists = self.sp.artist_related_artists(artist_id)
            return artists['artists']
        except Exception as e:
            print(f"Error retrieving related artists from Spotify: {e}")
            return None

    def get_user_profile(self, user_id):
        """Retrieves a user's profile information."""
        try:
            profile = self.sp.user(user_id)
            return profile
        except Exception as e:
            print(f"Error retrieving user profile from Spotify: {e}")
            return None

    def get_user_top_tracks(self, user_id, time_range='medium_term'):
        """Retrieves a user's top tracks."""
        try:
            top_tracks = self.sp.current_user_top_tracks(time_range=time_range, limit=50)
            return top_tracks['items']
        except Exception as e:
            print(f"Error retrieving user's top tracks from Spotify: {e}")
            return None