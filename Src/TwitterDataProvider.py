from TwitterSearch import *

CONSUMER_KEY = '5vm38GTOO8WWFOqNRTMOiQ'
CONSUMER_SECRET = 'pzokQ4JJNe4WVApB4Rc1tGe2xWWNlk7BeSkaS5Oa5Y'
ACCESS_TOKEN = '825058345-QngBxmsQKT22KOMlUYF8Ca2nu3cFt6E9dGU63F7A'
ACCESS_TOKEN_SECRET = 'Xd08I1vSOqQIalHm5LJjTjCFxoXWYh6zXgqZ5xeJI'

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
