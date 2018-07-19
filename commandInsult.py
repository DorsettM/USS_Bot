import discord
import random
from discord.ext import commands

def insults():
    
    #load in insults form a file
    insults = open('/home/INSULTS.txt', 'r').readlines()

    index = random.randint(0 , len(insults))
    
    text = insults[index]

    return text

    
