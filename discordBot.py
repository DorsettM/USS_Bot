#!/usr/bin/python3
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
    embed = discord.Embed(title="USS Bot" , description="The Mighty Bot", color=0x000000)

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
        # await bot.say(person.mention)
        await bot.say(person.mention + ' ' + text.format(ctx.message))

#declare stats command
@bot.command(pass_context=True)
async def stats(ctx, username):

    #call stats function
    STATS = getStats(username)
    win_rate = STATS['win_rate']
    win_rate = '{0:.2%}'.format(win_rate)
    


    if STATS['win_rate'] < 0.45:
        descrip = 'Bad'
    elif STATS['win_rate'] >= 0.45 and STATS['win_rate'] < 0.50:
        descrip = 'Average'
    elif STATS['win_rate'] >= 0.50 and STATS['win_rate'] < 0.54:
        descrip = 'Good'
    elif STATS['win_rate'] >= 0.54 and STATS['win_rate'] < 0.57:
        descrip = 'Very Good'
    elif STATS['win_rate'] >= 0.57 and STATS['win_rate'] < 0.60:
        descrip = 'Unicum'
    else:
        descrip = 'Super Unicum'

    #embed stats to be displayed
    embed = discord.Embed(title= username, description = descrip, color=0x000000)
    embed.add_field(name = 'Win Rate' , value = win_rate, inline = True)
    embed.add_field(name = 'Battles' , value = STATS['battles'] , inline = True)
    embed.add_field(name='Average XP', value = STATS['avg_xp'], inline = True)
    embed.add_field(name = 'Max XP Earned', value = STATS['max_xp'], inline = True)
    embed.add_field(name = 'Average Damage', value = STATS['avg_damage'], inline = True)
    embed.add_field(name = 'Max Damage Dealt', value = STATS['max_damage_dealt'], inline = True)
    embed.add_field(name = 'Max Damage Ship' , value = STATS['max_damage_ship'] , inline = False)
    embed.set_image(url = STATS['max_damage_ship_image'])

    await bot.say(embed=embed)
    

#declare WAR function
@bot.command(pass_context=True)
async def war(ctx):
    await bot.say('War Were Declared'.format(ctx.message))
   # author = ctx.message.author.voice.voice_channel
   # link = 'https://www.youtube.com/watch?v=TS3kiRYcDAo'
   # voice = await bot.join_voice_channel(author)
   # player = await voice.create_ytdl_player(link)
   # player.start()


@bot.command(pass_context=True)
async def update(ctx):


    syst = call('git ' + 'pull', shell = True)
    
    
    
    os.execv('/home/discordBot/USS_Bot/discordBot.py', sys.argv)






#remove built in help command to declare our own
bot.remove_command('help')




#declare help command
@bot.command(pass_context=True)
async def help(ctx, command):
    
    if(command == ''):
        command = 'all'

    #create embed object
    embed = discord.Embed(title = 'USS Bot' , description = 'Armament:' , color = 0x000000)
    

    #Switch command to print function of command or all if command is not given
    if command in ('!hello' , 'hello'):
        embed.add_field(name = '!hello' , value = 'Says hello' , inline = False)
    elif command in ('!history' , 'history'):
        embed.add_field(name = '!history' , value = 'Tells you what happened today in naval history' , inline = False)
    elif command in ('!war' , 'WAR'):
        embed.add_field(name = '!WAR' , value = 'Soon war were delcared' , inline = False)
    elif command in ('!help' , 'help'):
        embed.add_field(name = '!help command' , value = 'This is how you do it' , inline = False)
    elif command in ('!insult', 'insult'):
        embed.add_field(name = '!insult person' , value = 'Insult someone' , inline = False)
    elif command in ('!stats' , 'stats'):
        embed.add_field(name='!stats username' , value=' displays World of Warships Stats', inline = False)
    elif command == 'all':
        embed.add_field(name = '!hello' , value = 'Says hello' , inline = False)
        embed.add_field(name = '!history' , value = 'Tells you what happened today in naval history' , inline = False)
        embed.add_field(name = '!WAR' , value = 'Soon war were delcared' , inline = False)
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


