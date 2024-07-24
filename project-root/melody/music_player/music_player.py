import discord
from discord.ext import commands
import asyncio
import youtube_dl
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import soundcloud
from soundcloud.resource import Resource
import ffmpeg
from pydub import AudioSegment

# Suppress noisy youtube_dl logging
youtube_dl.utils.bug_reports_message = lambda: ''

class Song:
    def __init__(self, title, url, source):
        self.title = title
        self.url = url
        self.source = source

    async def get_audio_stream(self):
        if self.source == "youtube":
            return await self.get_youtube_audio_stream()
        elif self.source == "spotify":
            return await self.get_spotify_audio_stream()
        elif self.source == "soundcloud":
            return await self.get_soundcloud_audio_stream()

    async def get_youtube_audio_stream(self):
        try:
            # Use youtube-dl to download and extract the audio stream
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
                'noplaylist': True,
                'nocheckcertificate': True,
                'ignoreerrors': True,
                'logtostderr': False,
                'quiet': True,
                'no_warnings': True,
                'default_search': 'auto',
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(self.url, download=False)
                audio_url = info['formats'][0]['url']
            return audio_url
        except Exception as e:
            print(f"Error getting YouTube audio stream: {e}")
            return None

    async def get_spotify_audio_stream(self):
        try:
            # Use spotipy to get track information and audio URL
            client_credentials_manager = SpotifyClientCredentials(
                client_id="your_spotify_client_id",
                client_secret="your_spotify_client_secret"
            )
            sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
            track_info = sp.search(q=self.url, type='track', limit=1)
            track_uri = track_info['tracks']['items'][0]['uri']
            audio_features = sp.audio_features(track_uri)
            audio_url = audio_features[0]['preview_url']
            return audio_url
        except Exception as e:
            print(f"Error getting Spotify audio stream: {e}")
            return None

    async def get_soundcloud_audio_stream(self):
        try:
            # Use soundcloud-python to get track information and audio URL
            client = soundcloud.Client(client_id="your_soundcloud_client_id", client_secret="your_soundcloud_client_secret")
            track = client.get('/resolve', url=self.url)
            audio_url = track.stream_url
            return audio_url
        except Exception as e:
            print(f"Error getting SoundCloud audio stream: {e}")
            return None

class MusicPlayer:
    def __init__(self):
        self.queue = []
        self.current_song = None
        self.voice_client = None
        self.is_playing = False
        self.is_looping = False

    async def play(self, ctx, query):
        # Identify the source of the query (YouTube, Spotify, SoundCloud)
        source = self.get_source(query)

        if source:
            # Create a Song object
            song = Song(title=query, url=query, source=source)

            # Add the song to the queue
            self.queue.append(song)

            # Start playback if the queue is empty
            if not self.is_playing:
                await self.queue_next(ctx)
        else:
            await ctx.send("Invalid song source. Please provide a valid YouTube, Spotify, or SoundCloud link or search term.")

    async def queue_next(self, ctx):
        if self.voice_client and self.queue:
            self.is_playing = True
            self.current_song = self.queue.pop(0)
            audio_stream = await self.current_song.get_audio_stream()
            if audio_stream:
                # Convert to audio segment
                audio_segment = AudioSegment.from_file(audio_stream)
                audio_segment = audio_segment.set_frame_rate(48000)  # Set to a consistent frame rate
                audio_source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(audio_stream, before_options="-vn -ac 2 -af lowpass=f=4000"), volume=0.5)
                self.voice_client.play(audio_source, after=lambda e: asyncio.run_coroutine_threadsafe(self.queue_next(ctx), loop=ctx.bot.loop))
                await ctx.send(f"Now playing: {self.current_song.title}")
            else:
                await ctx.send("Error playing the song. Please try again later.")
        else:
            self.is_playing = False

    def get_queue(self, ctx):
        return self.queue

    def get_current_song(self, ctx):
        return self.current_song

    async def pause(self, ctx):
        if self.voice_client and self.voice_client.is_playing():
            self.voice_client.pause()
            await ctx.send("Playback paused.")
        else:
            await ctx.send("No song is currently playing.")

    async def resume(self, ctx):
        if self.voice_client and self.voice_client.is_paused():
            self.voice_client.resume()
            await ctx.send("Playback resumed.")
        else:
            await ctx.send("The song is not paused.")

    async def skip(self, ctx):
        if self.voice_client and self.voice_client.is_playing():
            self.voice_client.stop()
            await ctx.send("Skipped to the next song.")
            await self.queue_next(ctx)
        else:
            await ctx.send("No song is currently playing.")

    async def stop(self, ctx):
        if self.voice_client and self.voice_client.is_playing():
            self.voice_client.stop()
            self.queue.clear()
            self.current_song = None
            self.is_playing = False
            await ctx.send("Playback stopped and queue cleared.")
        else:
            await ctx.send("No song is currently playing.")

    async def set_volume(self, ctx, volume):
        if self.voice_client:
            self.voice_client.source.volume = volume / 100
            await ctx.send(f"Volume set to {volume}%")
        else:
            await ctx.send("Not connected to a voice channel.")

    async def loop(self, ctx):
        self.is_looping = not self.is_looping
        if self.is_looping:
            await ctx.send("Looping enabled.")
        else:
            await ctx.send("Looping disabled.")

    async def connect_voice(self, ctx):
        if ctx.author.voice:
            self.voice_client = await ctx.author.voice.channel.connect()
            await ctx.send("Connected to voice channel.")
        else:
            await ctx.send("You are not connected to a voice channel.")

    async def disconnect_voice(self, ctx):
        if self.voice_client:
            await self.voice_client.disconnect()
            self.voice_client = None
            await ctx.send("Disconnected from voice channel.")
        else:
            await ctx.send("Not connected to a voice channel.")

    def get_source(self, query):
        if "youtube.com" in query or "youtu.be" in query:
            return "youtube"
        elif "open.spotify.com" in query:
            return "spotify"
        elif "soundcloud.com" in query:
            return "soundcloud"
        else:
            return None