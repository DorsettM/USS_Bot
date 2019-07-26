#!/usr/bin/python3
from player import *
import discord
from discord.ext import commands
from commandHistory import History
from commandInsult import insults
from commandStats import getStats
import asyncio 
import subprocess
from subprocess import call
import os
import sys



queue = {}

#Read in token from file
f = open('/home/TOKEN.txt', "r")
TOKEN = f.read().replace('\n','')
f.close()


#declare the bot
bot = commands.Bot(command_prefix='!')



#declare hello command
@bot.command(pass_context=True)
async def hello(ctx):
        await bot.say('Hello! {0.author.mention} '.format(ctx.message))



#declare goodbye command
@bot.command(pass_context=True)
async def goodbye(ctx):
    await bot.close()



#declare info command
@bot.command(pass_context=True)
async def info(ctx):
    #embed info in discord, title, description, text color
    embed = discord.Embed(title="USS Bot" , description="The Mighty Bot", color=0xff0000)

    #embed author section
    embed.add_field(name="Author", value="Napoleon3500")
    await bot.say(embed=embed)



#declare history function
@bot.command(pass_context=True)
async def history(ctx):
    #see commandHistory.py
    text = History()
    await bot.say(text.format(ctx.message))



#declare insult command
@bot.command(pass_context=True)
async def insult(ctx, person:discord.Member = None):
    
    f = ctx.message.server.me    
    if person == f:
        await bot.say("You're not as funny as you think...".format(ctx.message))
    else:
        text = insults()
        await bot.say(person.mention + ' ' + text.format(ctx.message))

#declare stats command
@bot.command(pass_context=True)
async def stats(ctx, username):

    #call stats function
    try:
        player1 = getStats(username)
    except:
        await bot.say("Player was not found!")
    embed = player1.createEmbed()
    await bot.say(embed=embed)
    

    del player1
    
    



@bot.command(pass_context=True)
async def update(ctx):

    


    syst = call('git ' + 'pull ' + 'https://github.com/DorsettM/USS_Bot' , shell = True)
    
    if syst == 0:
       await bot.say('Update Sucessful'.format(ctx.message))
    
    os.execv('/home/discordBot/discordBot.py', sys.argv)



@bot.command(pass_context=True)
async def play(ctx, song):
    
    server = ctx.message.server

    if bot.is_voice_connected(server) == False:
        channel = ctx.message.author.voice.voice_channel
        voice = await bot.join_voice_channel(channel)

    player = await voice.create_ytdl_player(song)

    queue[server].append(player)
    player.start()


#remove built in help command to declare our own
bot.remove_command('help')




#declare help command
@bot.command(pass_context=True)
async def help(ctx, command=None):
    
    if(command == None):
        command = 'all'

    #create embed object
    embed = discord.Embed(title = 'USS Bot' , description = 'Armament:' , color = 0x000000)
    

    #Switch command to print function of command or all if command is not given
    if command in ('!hello' , 'hello'):
        embed.add_field(name = '!hello' , value = 'Says hello' , inline = False)
    elif command in ('!history' , 'history'):
        embed.add_field(name = '!history' , value = 'Tells you what happened today in naval history' , inline = False)
    elif command in ('!help' , 'help'):
        embed.add_field(name = '!help command' , value = 'This is how you do it' , inline = False)
    elif command in ('!insult', 'insult'):
        embed.add_field(name = '!insult person' , value = 'Insult someone' , inline = False)
    elif command in ('!stats' , 'stats'):
        embed.add_field(name='!stats username' , value=' displays World of Warships Stats', inline = False)
    elif command == 'all':
        embed.add_field(name = '!hello' , value = 'Says hello' , inline = False)
        embed.add_field(name = '!history' , value = 'Tells you what happened today in naval history' , inline = False)
        embed.add_field(name = '!insult person' , value = 'Insult someone' , inline = False)
        embed.add_field(name='!stats username' , value=' displays World of Warships Stats', inline = False)
        embed.add_field(name = '!help command' , value = 'This is how you do it' , inline = False)



    await bot.say(embed=embed)


@bot.event
async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')



#start the bot
bot.run(TOKEN)

