from twython import Twython, TwythonError
from secrets import *
import re
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#Setting Twitter's search results as a variable

query = ' (\__/)   ||              (•ㅅ•)   ||             /  　  づ'
search_results = twitter.search(lang='en', q=query, count=100, result_type='popular')

def is_public(status):
    if status['retweet_count'] >20 or status['user']['followers_count'] >10000:
        return True
    else:
        return False

tweet_counter=0

for tweet in search_results["statuses"]:
        if is_public(tweet):
                try:
                    if tweet_counter ==0:
                        user = tweet['user']['screen_name']
                        id = tweet['id']
                        tweet_url = f'https://twitter.com/{user}/status/{id}'
                        twitter.retweet(id=tweet['id'])
                        tweet_counter +=1
                except TwythonError:
                    continue
