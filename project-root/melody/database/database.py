import pymongo
from pymongo import MongoClient

class Database:
    def __init__(self, database_uri, database_name):
        self.database_uri = database_uri
        self.database_name = database_name
        self.client = None
        self.db = None

    def connect(self):
        """Connects to the MongoDB database."""
        try:
            self.client = MongoClient(self.database_uri)
            self.db = self.client[self.database_name]
            print(f"Connected to MongoDB database: {self.database_name}")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def create_playlist(self, playlist_name, user_id):
        """Creates a new playlist in the database."""
        try:
            playlist = {
                "name": playlist_name,
                "user_id": user_id,
                "songs": []
            }
            self.db.playlists.insert_one(playlist)
            print(f"Created playlist: {playlist_name}")
        except Exception as e:
            print(f"Error creating playlist: {e}")

    def add_song_to_playlist(self, playlist_name, song_title, song_url, user_id):
        """Adds a song to an existing playlist."""
        try:
            playlist = self.db.playlists.find_one({"name": playlist_name, "user_id": user_id})
            if playlist:
                song = {
                    "title": song_title,
                    "url": song_url
                }
                self.db.playlists.update_one(
                    {"name": playlist_name, "user_id": user_id},
                    {"$push": {"songs": song}}
                )
                print(f"Added song '{song_title}' to playlist: {playlist_name}")
            else:
                print(f"Playlist '{playlist_name}' not found.")
        except Exception as e:
            print(f"Error adding song to playlist: {e}")

    def get_playlist(self, playlist_name, user_id):
        """Retrieves a playlist based on its name."""
        try:
            playlist = self.db.playlists.find_one({"name": playlist_name, "user_id": user_id})
            if playlist:
                return playlist
            else:
                return None
        except Exception as e:
            print(f"Error getting playlist: {e}")

    def delete_playlist(self, playlist_name, user_id):
        """Deletes a playlist."""
        try:
            result = self.db.playlists.delete_one({"name": playlist_name, "user_id": user_id})
            if result.deleted_count > 0:
                print(f"Deleted playlist: {playlist_name}")
            else:
                print(f"Playlist '{playlist_name}' not found.")
        except Exception as e:
            print(f"Error deleting playlist: {e}")

    def save_user_data(self, user_id, user_data):
        """Saves user data (e.g., preferences) to the database."""
        try:
            self.db.users.update_one(
                {"_id": user_id},
                {"$set": user_data},
                upsert=True
            )
            print(f"Saved user data for user ID: {user_id}")
        except Exception as e:
            print(f"Error saving user data: {e}")

    def get_user_data(self, user_id):
        """Retrieves user data from the database."""
        try:
            user_data = self.db.users.find_one({"_id": user_id})
            return user_data
        except Exception as e:
            print(f"Error getting user data: {e}")