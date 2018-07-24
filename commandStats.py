import requests
from bs4 import BeautifulSoup
import json

FINAL = {}
SHIPS = {}



def getRequest(url):
    
    #request information from wargaming
    wargaming = requests.get(url)
    c = wargaming.content
    soup = BeautifulSoup(c)
    info = json.loads(str(soup))
    info = info['data']
    return info


def getStats(username):

    #This is the return dictionary to be used by the bot command
    FINAL = {}


    #Get wargaming API id fromt ext file
    f = open('/home/WARGAMING.txt')
    app_id = f.read().replace('\n' , '')
    f.close()


    #list of ships and ship stats
    url = 'https://api.worldofwarships.com/wows/encyclopedia/ships/?application_id=' + app_id
    SHIPS = getRequest(url)
    
    
    #URL to get account_id
    url = 'https://api.worldofwarships.com/wows/account/list/?application_id=' + app_id + '&search=' + username
    
    #Get account_id from wargaming player information
    arr = getRequest(url)
    temp = arr[0]
    account_id = str(temp['account_id'])
    



    #Use account_id to obtain stats from wargaming
    #this returns way more information than anyone could ever need
    url = 'https://api.worldofwarships.com/wows/account/info/?application_id=' + app_id + '&account_id=' + account_id +'&extra=statistics.pvp_solo'
    
    #Break down information into individual variables
    arr = getRequest(url)
    temp = arr[account_id]
    temp2 = temp['statistics']
    temp3 = temp2['pvp']

    #games variable is needed to calculate other stats
    games = temp3['battles']


    #get variables
    wins = temp3['wins']
    losses = temp3['losses']

    xp = temp3['xp']

    max_xp = temp3['max_xp']
    max_xp_ship = temp3['max_xp_ship_id']
    
    max_damage_dealt = temp3['max_damage_dealt']
    max_damage_ship = temp3['max_damage_dealt_ship_id']
    
    damage_dealt = temp3['damage_dealt']

    #calculate stats
    win_rate = wins/games
    avg_xp = xp/games
    avg_damage = damage_dealt/games

    #add variables to return dictionary
    FINAL['win_rate'] = (win_rate)
    FINAL['max_xp'] = max_xp
    FINAL['avg_xp'] = int(avg_xp)
    FINAL['max_damage_dealt'] = max_damage_dealt
    FINAL['avg_damage'] = '{0:.2f}'.format(avg_damage)
    

    #Ship IDs are broken??
    #FINAL['max_xp_ship'] = SHIPS[max_xp_ship]
    #FINAL['max_damage_ship'] = SHIPS[max_damage_ship] 
    

    return FINAL


