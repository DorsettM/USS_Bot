import requests
from bs4 import BeautifulSoup
import json

FINAL = {}



def getRequest(url):
    
    #request information from wargaming
    wargaming = requests.get(url)
    c = wargaming.content
    soup = BeautifulSoup(c, 'html.parser')
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
    max_xp_ship_id = temp3['max_xp_ship_id']
    
    max_damage_dealt = temp3['max_damage_dealt']
    max_damage_ship = temp3['max_damage_dealt_ship_id']
    
    #request information on max damage ship 
    
    
    url = 'https://api.worldofwarships.com/wows/encyclopedia/ships/?application_id=' + app_id + '&ship_id=' + str(max_damage_ship) + ''

    max_damage_ship_info = getRequest(url)
    max_damage_ship_info = max_damage_ship_info[str(max_damage_ship)]
    if 'null' in max_damage_ship_info:
        max_damage_ship_name = 'Not Found'
        max_damage_ship_image = 'http://www.51allout.co.uk/wp-content/uploads/2012/02/Image-not-found.gif'
    else:
        max_damage_ship_image = max_damage_ship_info['images']
        max_damage_Ship_image = max_damage_ship_image['small']
        max_damage_ship_name = max_damage_ship_info['name']

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
    FINAL['max_damage_ship'] = max_damage_ship_name
    FINAL['max_damage_ship_image'] = max_damage_ship_image['small']
    FINAL['avg_damage'] = '{0:.2f}'.format(avg_damage)
    FINAL['battles'] = games
    
    

    return FINAL


