import discord
from discord.ext import commands
from commandHistory import History
from commandInsult import insults
import asyncio 


#Read in token from file
f = open('/home/TOKEN.txt', "r")
TOKEN = f.read().replace('\n','')
f.close()


#declare the bot
bot = commands.Bot(command_prefix='!')

client = discord.Client()


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
    text = insults()
   # await bot.say(person.mention)
    await bot.say(person.mention + ' ' + text.format(ctx.message))



#declare WAR function
@bot.command(pass_context=True)
async def WAR(ctx):
    await bot.say('War Were Declared'.format(ctx.message))
   # author = ctx.message.author.voice.voice_channel
   # link = 'https://www.youtube.com/watch?v=TS3kiRYcDAo'
   # voice = await bot.join_voice_channel(author)
   # player = await voice.create_ytdl_player(link)
   # player.start()








#remove built in help command to declare our own
bot.remove_command('help')


#declare help command
@bot.command(pass_context=True)
async def help(ctx, command):
    
    #create embed object
    embed = discord.Embed(title = 'USS Bot' , description = 'Armament:' , color = 0x000000)
    

    #Switch command to print function of command or all if command is not given
    if command in ('!hello' , 'hello'):
        embed.add_field(name = '!hello' , value = 'Says hello' , inline = False)
    elif command in ('!history' , 'history'):
        embed.add_field(name = '!history' , value = 'Tells you what happened today in naval hostory' , inline = False)
    elif command in ('!WAR' , 'WAR'):
        embed.add_field(name = '!WAR' , value = 'Soon war were delcared' , inline = False)
    elif command in ('!help' , 'help'):
        embed.add_field(name = '!help command' , value = 'This is how you do it' , inline = False)
    elif command in ('!insult', 'insult'):
        embed.add_field(name = '!insult person' , value = 'Insult someone' , inline = False)
    elif command == 'all':
        embed.add_field(name = '!hello' , value = 'Says hello' , inline = False)
        embed.add_field(name = '!history' , value = 'Tells you what happened today in naval hostory' , inline = False)
        embed.add_field(name = '!WAR' , value = 'Soon war were delcared' , inline = False)
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


