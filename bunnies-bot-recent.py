from twython import Twython, TwythonError
from secrets import *
import re
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#Setting Twitter's search results as a variable

query = ' (\__/)   ||              (•ㅅ•)   ||             /  　  づ'
search_results = twitter.search(lang='en', q=query, count=100)

def is_public(status):
    if status['retweet_count'] > 20 or status['user']['followers_count'] >10000:
        return True
    else:
        return False

def is_bunny(status):
    """
    Determines whether or not the tweet is a bunny holding a sign,
    using the same list of queries that the streaming API uses.
    """
    test_text = ' '.join(status['text'].lower().split()) # Remove capital letters and excessive whitespace/linebreaks
    usernames = [''] # Block screen_names of known parody accounts
    if status['user']['screen_name'] not in usernames and all(u not in status['text'] for u in usernames):
        if '|' in test_text: # Capture parodies of the form
            return True
        else:
            return False
    else:
        return False


tweet_counter=0

for tweet in search_results["statuses"]:
        if is_public(tweet):
            #if "RT @" not in tweet['text']:
                try:
                    if tweet_counter ==0:
                    #if tweet_counter <20:
                        user = tweet['user']['screen_name']
                        id = tweet['id']
                        tweet_url = f'https://twitter.com/{user}/status/{id}'
                        #twitter.update_status(status=tweet_url)
                        twitter.retweet(id=tweet['id'])
                        #print(tweet['text'], tweet_url)
                        tweet_counter +=1
                except TwythonError:
                    continue
