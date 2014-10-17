from twython import Twython #http://twython.readthedocs.org/en/latest/
    # used http://www.craigaddyman.com/mining-all-tweets-with-python/
import time
import requests
from collections import OrderedDict


REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "K7ddHMoZcHXu0WyWdnp6wdQxf"
CONSUMER_SECRET = "OcvSpsGJ5e1f9GvHbT1y5TXLzwETVkL9wkd1WDzL3FHgC7WDzk"

ACCESS_KEY = "2539409241-FFZPA5lh2vZklUx3q5jASFesRVVXPxqfS6nY8QB"
ACCESS_SECRET = "zzQVXih1Gy2cR1WdMtcMhmXbWpi1S45Jc7vlLlkHFWwm9"

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)




user_Friends = twitter.get_friends_list(screen_name="Francis_Pruter", count=200, skip_status='true', include_user_entities='false')

ctr = 1

fcountlist={}

for friend in user_Friends['users']:
  fcountlist[friend['name']] = friend['friends_count']
  ctr = ctr+1

fcountlist["ME"] = ctr-1

#sort list by friend count https://docs.python.org/2/library/collections.html#ordereddict-examples-and-recipes

fcountlist = OrderedDict(sorted(fcountlist.items(), key=lambda t: t[1]))

print fcountlist

ctr=1
with open('friendslist', 'w+') as f:
  for friend in fcountlist:
    f.write( str(ctr) + ":" + friend + ':' + str(fcountlist[friend]) + '\n' )
    ctr=ctr+1








