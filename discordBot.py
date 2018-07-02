import discord
from discord.ext import commands
from commandHistory import History


f = open('/home/root1/Desktop/USS_Bot/token.txt', "r")
TOKEN = f.read().replace('\n','')
f.close()

bot = commands.Bot(command_prefix='!')




@bot.command()
async def hello(ctx):
        await ctx.send('Hello! {0.author.mention} '.format(ctx.message))



@bot.command()
async def goodbye(ctx):
    await bot.close()


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="USS Bot" , description="The Mighty Bot", color=0x000000)
    embed.add_field(name="Author", value="Napoleon3500")
    await ctx.send(embed=embed)


@bot.command()
async def history(ctx):
    text = History()
    await ctx.send(text.format(ctx.message))

@bot.command()
async def WAR(ctx):
    await ctx.send('War Were Declared'.format(ctx.message))
    

    
@bot.event
async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')


bot.run(TOKEN)


