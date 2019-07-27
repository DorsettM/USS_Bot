import requests
from bs4 import BeautifulSoup
import traceback


def History():

	try:
		#link to the navy history page
		link_page = 'http://www.navy.mil/search/display_history.asp'

		#go get the page
		page = requests.get(link_page)

		#Parse the page and return the desired element
		soup = BeautifulSoup(page.text, 'html.parser')
		name_box = soup.find(class_='storybody')
		name = name_box.get_text()
	
	except Exception as e:
		traceback.print_exc()
	
	return name


History()
