#!/usr/bin/python
import cgitb
import json
import urllib
import sys
import os
import random
from bs4 import BeautifulSoup
from unauth import make_soup, check_request, create_json 

cgitb.enable(format='txt')  										#i can has error reporting
print 'Content-Type: text/plain\n'  								#gotta have a blank line after the header
	

#checking URL for parameters
bust_cache = random.getrandbits(64) 								#random number to avoid caching
is_realtime = ''													
raw_query = os.environ['QUERY_STRING'] 								
checked_query = check_request('query', raw_query)
submitted = checked_query.partition('&')

if submitted[2]:
	tail = str(submitted[2]).partition('&')
	total = int(tail[0])
	if tail[2]:
		is_realtime = 'realtime'
else:
	total = 0
query = urllib.unquote(submitted[0])


#create list of URLs to tweets
user_soup = make_soup('https://twitter.com/search/' + is_realtime + '?q=' + query + '&' + str(bust_cache))
result = user_soup.find_all('a', class_='details with-icn js-details')

#checking to make sure we have enough results to fill the total, supplying number if not.
check_result = len(result)

if check_result == 0:
	print '{"error":"No results","description":"Your search did not return any Tweets"}'
	sys.exit()
	
if check_result < total or total == 0:
	total = check_result

#printing the result
count = 0
print '{"searchResults":{'
while count <= total - 1:
	print '"searchTweet":' + str(count) +','
	tweet_soup = make_soup('http://twitter.com' + result[count]['href'])
	clean_json = create_json(tweet_soup)
	print '"tweetContent":'+ clean_json
	count += 1 
	if count == total:
		print '}'
	else:
		print '},'
