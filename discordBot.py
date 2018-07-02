import discord
from discord.ext import commands
from commandHistory import History

#Read in token from file
f = open('/home/root1/Desktop/USS_Bot/token.txt', "r")
TOKEN = f.read().replace('\n','')
f.close()


#declare the bot
bot = commands.Bot(command_prefix='!')



#declare hello command
@bot.command()
async def hello(ctx):
        await ctx.send('Hello! {0.author.mention} '.format(ctx.message))



#declare goodbye command
@bot.command()
async def goodbye(ctx):
    await bot.close()



#declare info command
@bot.command()
async def info(ctx):
    #embed info in discord, title, description, text color
    embed = discord.Embed(title="USS Bot" , description="The Mighty Bot", color=0x000000)

    #embed author section
    embed.add_field(name="Author", value="Napoleon3500")
    await ctx.send(embed=embed)



#declare history function
@bot.command()
async def history(ctx):
    #see commandHistory.py
    text = History()
    await ctx.send(text.format(ctx.message))



#declare WAR function
@bot.command()
async def WAR(ctx):
    await ctx.send('War Were Declared'.format(ctx.message))
    

#remove built in help command to declare our own
bot.remove_command('help')


#declare help command
@bot.command()
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
    elif command == 'all':
        embed.add_field(name = '!hello' , value = 'Says hello' , inline = False)
        embed.add_field(name = '!history' , value = 'Tells you what happened today in naval hostory' , inline = False)
        embed.add_field(name = '!WAR' , value = 'Soon war were delcared' , inline = False)
        embed.add_field(name = '!help command' , value = 'This is how you do it' , inline = False)



    await ctx.send(embed=embed)


@bot.event
async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')




#start the bot
bot.run(TOKEN)


