import json
import urllib2
import random
from bs4 import BeautifulSoup

#taking your twitter page and making it a BeautifulSoup object
def make_soup(url):
	try:
		source = urllib2.urlopen(url).read()
		soup = BeautifulSoup(source)
		return soup
	except:
		print '{"error":"HTTPError","description":"Something went awry when we tried to contact Twitter"}'
		sys.exit()
		
#takes a soup object where the JSON is hiding and makes it clean	
def create_json(soup):  											
	tweet_json = soup.find('input', id='init-data')
	clean_json = json.dumps(json.loads(tweet_json['value']))
	return clean_json

#checks to make sure url isn't all messed up
def check_request(prefix, query):
	letters = (len(prefix) + 1)
	if query[:letters] == prefix + '=':
		user_name = query[letters:]
		return user_name
	else:
		print '{"error":"URLError","description":"We didn\'t like the request you sent. Please read the docs and try again."}'
		sys.exit()