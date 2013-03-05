#!/usr/bin/python
#Use this for your thing that you're gonna make
import cgitb
import json
import urllib2
import random
import os
from bs4 import BeautifulSoup

cgitb.enable(format='txt')  #i can has error reporting
print 'Content-Type: text/plain\n'  #gotta have a blank line after the header

#taking your twitter page and making it a BeautifulSoup object
def make_soup(url):
	try:
		source = urllib2.urlopen(url).read()
		soup = BeautifulSoup(source)
		return soup
	except:
		print '{"error":"HTTPError","description":"Something went awry when we tried to contact Twitter"}'
		sys.exit()
	
user_name = os.environ['QUERY_STRING'] # by url
bust_cache = random.getrandbits(64) #random number to avoid caching

#find link to latest tweet
user_soup = make_soup('https://twitter.com/' + user_name + '?=' + str(bust_cache))
result = user_soup.find('input', id='init-data')
profile_json = json.loads(result['value'])

#is profile protected
if profile_json['profile_user']['protected'] == True:
	print '{"error":"Authentication Error","description":"This account is protected."}'
else:
	print json.dumps(profile_json, sort_keys=True, indent=4, separators=(',', ': '))



