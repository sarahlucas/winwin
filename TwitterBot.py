"""

A simple Twitter bot using the Twitter Python library that finds users who tweet about "Christmas gift ideas," 
favorites their tweet, follows the users and sends them a friendly tweet with Amazon links of popular gift ideas.
 
"""

import urllib
import simplejson
import twitter

consumer_key = 'pUT2bMKp4FvRYsmnd3ltjL3F3'
consumer_secret = 'DlMJi9gQQoACknh2QQiVZLtF2R5t6KM700k9SBV6zfB4FgIq2N'
access_token_key = '382811711-j0hkveej8kWWSUXuHta7GgSZMyPMGj2Tcn392nqx'
access_token_secret = 'npLdv4TMTppd1HbPfVGZTzO8cYM9KH3rsjPeh31hhxISL'

def searchTweets(query):
	search = urllib.urlopen("http://search.twitter.com/search.json?q="+query)
	dict = simplejson.loads(search.read())
	return dict

api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)
tweets = searchTweets("retweet+win&rpp=100&result_type=recent")


for i in range(len(tweets["results"])):
	tweeter = tweets["results"][i]["from_user"]
	status = twitter.Api.GetStatus(api, tweets["results"][i]["id"])
	api.CreateFavorite(status)
	api.CreateFriendship(tweeter)
	
