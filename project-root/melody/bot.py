import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from melody.music_player.music_player import MusicPlayer

load_dotenv()

# Get the Discord bot token from the environment variable
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Create an instance of the bot client
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Initialize the music player
music_player = MusicPlayer()

@bot.event
async def on_ready():
    """
    Event handler for when the bot is ready and connected to Discord.
    """
    print(f"Melody is online! Logged in as {bot.user}")

@bot.event
async def on_message(message):
    """
    Event handler for when a message is received from a user.
    """
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Process commands
    await bot.process_commands(message)

@bot.command()
async def play(ctx, *, query):
    """
    Plays a song from YouTube, Spotify, or SoundCloud.
    """
    # Join the voice channel if not already joined
    if not ctx.author.voice:
        await ctx.send("You are not connected to a voice channel.")
        return

    voice_channel = ctx.author.voice.channel
    if not bot.voice_clients:
        await voice_channel.connect()
    else:
        await bot.voice_clients[0].move_to(voice_channel)

    # Play the song
    await music_player.play(ctx, query)

@bot.command()
async def pause(ctx):
    """
    Pauses the current song.
    """
    await music_player.pause(ctx)

@bot.command()
async def resume(ctx):
    """
    Resumes playback.
    """
    await music_player.resume(ctx)

@bot.command()
async def skip(ctx):
    """
    Skips to the next song in the queue.
    """
    await music_player.skip(ctx)

@bot.command()
async def stop(ctx):
    """
    Stops playback and clears the queue.
    """
    await music_player.stop(ctx)

@bot.command()
async def queue(ctx):
    """
    Shows the current song queue.
    """
    queue = music_player.get_queue(ctx)
    if queue:
        await ctx.send(f"**Queue:**\n{', '.join([song.title for song in queue])}")
    else:
        await ctx.send("The queue is empty.")

@bot.command()
async def volume(ctx, volume: int):
    """
    Adjusts the playback volume.
    """
    await music_player.set_volume(ctx, volume)

@bot.command()
async def loop(ctx):
    """
    Toggles looping for the current song or queue.
    """
    await music_player.loop(ctx)

@bot.command()
async def connect(ctx):
    """
    Joins the voice channel you're in.
    """
    await music_player.connect_voice(ctx)

@bot.command()
async def disconnect(ctx):
    """
    Disconnects from the voice channel.
    """
    await music_player.disconnect_voice(ctx)

# Run the bot
bot.run(DISCORD_TOKEN)