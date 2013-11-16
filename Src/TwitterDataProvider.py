from TwitterSearch import *

import keyprovider

CONSUMER_KEY = keyprovider.getTwitterConsumerKey()
CONSUMER_SECRET = keyprovider.getTwitterConsumerSecret()
ACCESS_TOKEN = keyprovider.getTwitterAccessToken()
ACCESS_TOKEN_SECRET = keyprovider.getTwitterAccessTokenSecret()

def get_tweets(keyword, maxtweets=10):

    tweets = []
    try:
        searchOrder = TwitterSearchOrder()
        searchOrder.setKeywords([keyword])
        searchOrder.setLanguage('en')
        searchOrder.setCount(maxtweets) # only return 10 pages
        searchOrder.setIncludeEntities(False)
        # and don't give us all those entity information
        # Now let's create a Twitter Search API Object here
        # complete these by copying from your Twitter Application
        # from Twitter Developer Site
        ts = TwitterSearch(consumer_key = CONSUMER_KEY,consumer_secret = CONSUMER_SECRET,access_token = ACCESS_TOKEN,access_token_secret = ACCESS_TOKEN_SECRET)

        for tweet in ts.searchTweetsIterable(searchOrder):
            #print( tweet['text'] ) 
            tweets.append(tweet['text'])

    except Exception as e:
        print "Error in retrieving tweets !!\n"
        print (e)

    return tweets

get_tweets("Lucia Kannada Movie", 10)
