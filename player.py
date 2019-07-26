import discord
from discord.ext import commands


class Player:

    def __init__(self, winRate, maxXp, avgXp, maxDamageDealt, maxDamageShip, maxDamageShipImage, avgDamage, battles, username):
        self.winRate = winRate
        self.maxXp = maxXp
        self.avgXp = avgXp
        self.maxDamageDealt = maxDamageDealt
        self.maxDamageShip = maxDamageShip
        self.maxDamageShipImage = maxDamageShipImage
        self.avgDamage = avgDamage
        self.battles = battles
        self.username = username
        self.determineLeague(self.winRate)


    def determineLeague(self, winRate):
        
        winRate = winRate[0:len(winRate) -1]

        if float(winRate) < 45.00:
            self.color = 0xff0000
            self.league = 'Bad'
        elif float(winRate) >= 45.00 and float(winRate) < 50.00:
            self.color = 0xffa500
            self.league = 'Average'
        elif float(winRate) >= 50.00 and float(winRate) < 54.00:
            self.color = 0x00bfff
            self.league =  'Good'
        elif float(winRate) >= 54.00 and float(winRate) < 57.00:
            self.color = 0x008000
            self.league =  'Very Good'
        elif float(winRate) >= 57.00 and float(winRate) < 60.00:
            self.color = 0xff00ff
            self.league = 'Unicum'
        else:
            self. color = 0x800080
            self.league = 'Super Unicum'
        

    def createEmbed(self):

        embed = discord.Embed(title= self.username, description= self.league, color=self.color)
        embed.add_field(name = 'Win Rate' , value = self.winRate, inline = True)
        embed.add_field(name = 'Battles' , value = self.battles , inline = True)
        embed.add_field(name='Average XP', value = self.avgXp, inline = True)
        embed.add_field(name = 'Max XP Earned', value = self.maxXp, inline = True)
        embed.add_field(name = 'Average Damage', value = self.avgDamage, inline = True)
        embed.add_field(name = 'Max Damage Dealt', value = self.maxDamageDealt, inline = True)
        embed.add_field(name = 'Max Damage Ship' , value = self.maxDamageShip , inline = False)
        embed.set_image(url = self.maxDamageShipImage)

        return embed

    def __del__(self):
        print("Player deleted, thanks RNG")
        del self
