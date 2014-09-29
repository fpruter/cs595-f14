#extractTwitter.py
# Extracts 1000 URIs from timoreilly twitter page
# and prints its output to a file "uniqueURI"

from twython import Twython #http://twython.readthedocs.org/en/latest/
   # used http://www.craigaddyman.com/mining-all-tweets-with-python/
import time
import requests
from bs4 import BeautifulSoup

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "K7ddHMoZcHXu0WyWdnp6wdQxf"
CONSUMER_SECRET = "OcvSpsGJ5e1f9GvHbT1y5TXLzwETVkL9wkd1WDzL3FHgC7WDzk"

ACCESS_KEY = "2539409241-FFZPA5lh2vZklUx3q5jASFesRVVXPxqfS6nY8QB"
ACCESS_SECRET = "zzQVXih1Gy2cR1WdMtcMhmXbWpi1S45Jc7vlLlkHFWwm9"

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
lis = [] ## this is the latest starting tweet id

unique_URIs = []

################################################
#  This function tests to ensure the link is
#      unique and ensure it's a valid site
################################################

def testUniqueURL(link):
  try:
    r = requests.head(link, allow_redirects=True)
    if r.status_code == 200: #ensure valid website

        #tests to see if URI already saved in link
        if r.url in unique_URIs:
            return [False, ""]
        else:
            return [True, r.url]
    return [False, ""]
  except requests.ConnectionError:
    return [False, ""]


################################################
#  Extracts 1000 links from timoreilly's twitter
################################################
def get1000links():
    while True:
        uri = ""
    ## tweet extract method with the last list item as the max_id
        user_timeline = twitter.get_user_timeline(screen_name="timoreilly",
        count=200, include_retweets=False, max_id=lis[-1])

        for tweet in user_timeline:
            lis.append(tweet['id'])
            soup = BeautifulSoup(Twython.html_for_tweet(tweet))
            uri = soup.find('a', 'twython-url')
            if uri:
                uri = uri.get('href')
                unique = testUniqueURL(uri)
                if unique[0]:
                    unique_URIs.append(unique[1])
                    print 1000 - len(unique_URIs)
                    if len(unique_URIs) == 1000:
                        return
        print "Sleep for 5 minutes"
        time.sleep(300) ## 5 minute rest between api calls
###############################################

user_timeline = twitter.get_user_timeline(screen_name="timoreilly",count=1)
#print user_timeline

#print user_timeline[0]['id_str']
lis = [(user_timeline[0]['id_str'])]

get1000links()

f = open('uniqueURI', 'w')
            
for link in unique_URIs:
    f.write(link)
    f.write('\n')

f.close()