from bs4 import BeautifulSoup
import requests



def PLAY(search):

    url = 'https://www.youtube.com/results?search_query=' + search

    html = requests.get(url)

    f = html.content

    soup = BeautifulSoup(f, 'html.parser')

    links = soup.findAll('ytd-video-renderer class =')

    print(links)

PLAY('linkinpark')

