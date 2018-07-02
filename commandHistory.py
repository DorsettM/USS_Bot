import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup


def History():


    #link to the navy history page
    link_page = 'http://www.navy.mil/search/display_history.asp'

    #go get the page
    page = requests.get(link_page)

    
    soup = BeautifulSoup(page.text, 'html.parser')

    name_box = soup.find(class_='storybody')

    name = name_box.get_text()

    return name
