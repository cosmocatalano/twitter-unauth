#!/usr/bin/python
#returns a user's latest tweet with a single scrape
import cgitb
import json
import urllib
import sys
import os
import random
from bs4 import BeautifulSoup
from unauth import make_soup, check_request

cgitb.enable(format='txt')  								#error reporting on, in text
print 'Content-Type: text/plain\n' 							#specifies text, adds required after header info

#looking at the page URL for parameters
query = os.environ['QUERY_STRING']
user_name = urllib.unquote(check_request('name', query))
bust_cache = random.getrandbits(64) 						#random number to (try and) avoid caching

#find link to latest tweet
user_soup = make_soup('https://twitter.com/' + user_name + '?=' + str(bust_cache))
result = user_soup.find('input', id='init-data')
profile_json = json.loads(result['value'])

#print the result
print json.dumps(profile_json, sort_keys=True, indent=4, separators=(',', ': '))





