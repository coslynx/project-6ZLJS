# Melody Music Bot

## Project Overview

Melody is a Discord bot designed to provide a seamless and enjoyable music experience within Discord servers. The bot offers a range of features, including:

* **Music Playback:**  Play songs from YouTube, Spotify, and SoundCloud.
* **Queue Management:** Create and manage song queues.
* **Playback Controls:** Play, pause, skip, stop, resume, and repeat songs.
* **Voice Channel Integration:** Join, leave, and switch between voice channels.
* **Custom Playlists:** Create, save, and load personal playlists.
* **Lyrics Display:** (Optional) Display lyrics for currently playing songs.
* **Spotify Connect:** (Optional) Connect Spotify accounts to access personal music libraries and playlists.
* **User Roles and Permissions:** (Optional) Control bot access and features based on user roles.
* **Advanced Search:** (Optional) Search for songs by artist, album, lyrics, etc.

## Installation

1. **Install Python:** Make sure you have Python installed on your system. ([https://www.python.org/downloads/](https://www.python.org/downloads/))

2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain API keys:**
   * **Discord Bot Token:**
     * Create a new Discord bot application at [https://discord.com/developers/applications](https://discord.com/developers/applications).
     * Get your bot token from the "Bot" tab.
   * **YouTube Data API v3 Key:**
     * Create a new project on the Google Cloud Platform ([https://console.cloud.google.com/](https://console.cloud.google.com/)).
     * Enable the YouTube Data API v3 for your project.
     * Get your API key from the Google Cloud Console.
   * **Spotify API Credentials:**
     * Create a new Spotify developer account at [https://developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard/).
     * Create a new application and get your Client ID and Client Secret.
   * **SoundCloud API Credentials:**
     * Create a new SoundCloud developer account at [https://developers.soundcloud.com/](https://developers.soundcloud.com/).
     * Create a new application and get your Client ID and Client Secret.
   * **Genius API Key:** (Optional)
     * Create a new Genius account at [https://genius.com/](https://genius.com/).
     * Obtain an API key from [https://genius.com/api-clients](https://genius.com/api-clients).
   * **Musixmatch API Key:** (Optional)
     * Create a new Musixmatch account at [https://developer.musixmatch.com/](https://developer.musixmatch.com/).
     * Obtain an API key from your developer dashboard.

5. **Configure environment variables:**
   * Create a `.env` file in the project root directory.
   * Add the following lines, replacing the placeholders with your API keys:
     ```
     DISCORD_TOKEN=your_discord_bot_token
     YOUTUBE_API_KEY=your_youtube_api_key
     SPOTIFY_CLIENT_ID=your_spotify_client_id
     SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
     SOUNDCLOUD_CLIENT_ID=your_soundcloud_client_id
     SOUNDCLOUD_CLIENT_SECRET=your_soundcloud_client_secret
     GENIUS_API_KEY=your_genius_api_key  # (Optional)
     MUSIXMATCH_API_KEY=your_musixmatch_api_key  # (Optional)
     ```

## Running the Bot

1. **Start the bot:**
   ```bash
   python bot.py
   ```

2. **Add the bot to your Discord server:**
   * Go to the "OAuth2" tab in your Discord bot application.
   * Under "Scopes", enable the "bot" scope.
   * Click "Copy" next to the generated link.
   * Paste the link into your browser.
   * Authorize the bot to join your server.

## Commands

* **`!play [song name/URL]`:** Plays a song from YouTube, Spotify, or SoundCloud.
* **`!pause`:** Pauses the current song.
* **`!resume`:** Resumes playback.
* **`!skip`:** Skips to the next song in the queue.
* **`!stop`:** Stops playback and clears the queue.
* **`!queue`:** Shows the current song queue.
* **`!volume [number]`:** Adjusts the playback volume (0-100).
* **`!loop`:** Toggles looping for the current song or queue.
* **`!createplaylist [playlist name]`:** Creates a new playlist.
* **`!addsong [playlist name] [song name/URL]`:** Adds a song to a playlist.
* **`!saveplaylist [playlist name]`:** Saves a playlist to the database.
* **`!loadplaylist [playlist name]`:** Loads a playlist from the database.
* **`!lyrics`:** (Optional) Displays lyrics for the current song.
* **`!connect`:** (Optional) Joins the voice channel you're in.
* **`!disconnect`:** (Optional) Disconnects from the voice channel.

## Contributing

If you'd like to contribute to the Melody project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

## License

This project is licensed under the MIT License.