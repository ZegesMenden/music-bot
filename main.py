import os
import discord
import discord.utils
from datetime import datetime
from random import randint, choice
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
#stanbot

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

# changes the bots working location to where it is located
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('sex with stalin'))
    global music_loop
    music_loop = 0
    global guild
    guild = bot.get_guild(750805822992285747)
    global music_channel
    music_channel = discord.utils.get(guild.voice_channels, id=782065109350613052)
    print('poggy beginning')

@bot.command()
async def music(ctx):
    global music_channel
    await music_channel.connect()
    
    voice = discord.utils.get(bot.voice_clients, guild=guild)
    voice.volume = 75
    chose_next_song.start()
    global song_is_playing
    song_is_playing = 0
    global song_to_play
    song_to_play = 0
    

@tasks.loop(seconds=1)
async def chose_next_song():
    voice = discord.utils.get(bot.voice_clients, guild=guild)
    voice.volume = 100
    global song_is_playing
    global song_to_play
    if voice.is_playing() == True:
        song_is_playing = 1
    else:
        print('played a song')
        song_is_playing = 0
    if song_is_playing == 0:
        song_to_play += 1
        if song_to_play == 10:
            song_to_play = 0
        print('playing next song')
        voice.play(discord.FFmpegPCMAudio(f'({str(song_to_play)}).mp3'))
    
bot.run('')