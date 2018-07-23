import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests


def war(sub):

    page = 'https://www.reddit.com/r/' + sub

    html = requests.get(page)

    f = html.content

    soup = BeautifulSoup(f, 'html.parser')

    #images = soup.findAll('img')
    
    print(soup)
    
    
war('worldofwarships')
