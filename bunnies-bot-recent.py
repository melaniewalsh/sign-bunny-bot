from twython import Twython, TwythonError
from secrets import *
import re
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#Setting Twitter's search results as a variable

#query = ' (\__/)   ||              (•ㅅ•)   ||             /  　  づ'
query = '#HistorianSignBunny'
search_results = twitter.search(lang='en', q=query, count=100)

def is_public(status):
    if status['retweet_count'] > 20 or status['user']['followers_count'] >10000:
        return True
    else:
        return False

tweet_counter=0

for tweet in search_results["statuses"]:
        if is_public(tweet):
            if tweet_counter ==0:
                #if tweet_counter < 20:
                    try:
                        user = tweet['user']['screen_name']
                        id = tweet['id']
                        tweet_url = f'https://twitter.com/{user}/status/{id}'
                        twitter.retweet(id=tweet['id'])
                        #print(tweet['text'])
                        tweet_counter +=1
                    except TwythonError:
                        continue
