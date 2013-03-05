#!/usr/bin/python

import cgitb
import json
import urllib
import sys
import os
import random
from bs4 import BeautifulSoup
from unauth import make_soup, check_request, create_json 

cgitb.enable(format='txt')  							#error reporting on, text
print 'Content-Type: text/plain\n' 						#required blank line after headers

#checking URL for parameters
bust_cache = random.getrandbits(64) 					#cachebuster that may or may not work

query_string = os.environ['QUERY_STRING'] 	
checked_query = check_request('name', query_string)
submitted = checked_query.partition('&')

#checking for a number of tweets specified in the URL
try:
	if submitted[2]:
		total = int(submitted[2])
	else:
		total = 0
	user_name = urllib.unquote(submitted[0])
except:
	print '{"error":"URLError","description":"We didn\'t like the request you sent. Please read the docs and try again."}'
	sys.exit()

#find link to latest tweet
user_soup = make_soup('https://twitter.com/' + user_name + '?=' + str(bust_cache))
result = user_soup.find_all('a', class_='details with-icn js-details')
check_result = len(result)

#checking for no results
if check_result == 0:
	print '{"error":"No results","description":"This account has\'t produced any Tweets"}'

#supplying total number of results if URL parameter isn't going to work
if check_result < total or total == 0:
	total = check_result

#returning the number of tweets specified
count = 0
print '{"userResults":{'
while count <= total - 1:
	print '"userTweet":' + str(count) +','
	tweet_soup = make_soup('http://twitter.com' + result[count]['href'])
	clean_json = create_json(tweet_soup)
	print '"tweetContent":'+ clean_json
	count += 1 
	if count == total:
		print '}'
	else:
		print '},'


