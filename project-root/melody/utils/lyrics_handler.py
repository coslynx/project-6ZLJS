import requests
from bs4 import BeautifulSoup
from genius_lyrics_api import Genius

class LyricsHandler:
    """
    Handles retrieving song lyrics using Genius API.
    """
    def __init__(self, api_key):
        self.genius = Genius(api_key)
        self.base_url = "https://genius.com"

    def get_lyrics(self, song_title, artist_name=None):
        """
        Fetches lyrics for a song based on its title and optional artist name.

        Args:
            song_title (str): The title of the song.
            artist_name (str, optional): The name of the artist. Defaults to None.

        Returns:
            str: The lyrics of the song, if found. Otherwise, returns None.
        """
        try:
            song = self.genius.search_song(song_title, artist_name)
            if song:
                lyrics = song.lyrics
                return lyrics
            else:
                return None
        except Exception as e:
            print(f"Error retrieving lyrics from Genius: {e}")
            return None

    def search_lyrics(self, query):
        """
        Searches for lyrics based on a query string.

        Args:
            query (str): The search query.

        Returns:
            list: A list of song objects matching the query, if found. Otherwise, returns None.
        """
        try:
            results = self.genius.search_song(query)
            if results:
                return results
            else:
                return None
        except Exception as e:
            print(f"Error searching lyrics on Genius: {e}")
            return None

    def get_lyrics_from_url(self, url):
        """
        Retrieves lyrics from a Genius song URL.

        Args:
            url (str): The Genius song URL.

        Returns:
            str: The lyrics of the song, if found. Otherwise, returns None.
        """
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            lyrics_div = soup.find('div', class_='lyrics')
            if lyrics_div:
                lyrics = lyrics_div.get_text().strip()
                return lyrics
            else:
                return None
        except Exception as e:
            print(f"Error retrieving lyrics from Genius URL: {e}")
            return None