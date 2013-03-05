#Twitter unAuth

These Python scripts return wads of JSON from twitter.com based on usernames and strings. Those JSON objects can be programmatically processed in applications more or less in the same way as an API return.

They should also return errors as valid JSON objects. I make no guarantees on this.

This requires [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/) and a bunch of other things that probably came with your installation of Python.

There are basically three methods:


#The Latest Method

Returns the most recent tweet for a given user. If the given number is one, use the latest method instead

	/latest?name=[username]

Try it out:
[http://cosmocatalano.com/lab/twitter-scrape/user?name=@cosmocatalano&6](http://cosmocatalano.com/lab/twitter-scrape/user?name=@cosmocatalano&6)



#The User Method
Returns a certain number of tweets from a given user.

	/user?name=[username](&[integer])

Try it out:
[http://cosmocatalano.com/lab/twitter-scrape/user?name=@cosmocatalano&6](http://cosmocatalano.com/lab/twitter-scrape/user?name=@cosmocatalano&6)

#The Search Method
Returns a certain number of tweets containing a string. May be real time or not, though I'm not especially clear on the distinction.

	/search?query=[string](&[integer], defaults to all)(&['realtime'], default not realtime)

Try it out:
[http://cosmocatalano.com/lab/twitter-scrape/user?name=@cosmocatalano&6](http://cosmocatalano.com/lab/twitter-scrape/user?name=@cosmocatalano&6)