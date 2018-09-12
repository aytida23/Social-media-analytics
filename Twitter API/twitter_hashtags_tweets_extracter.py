"""
This is a twitter hashtags tweets extracter script written in
python 2.7x version using tweepy python library for accessing
the twitter API.
"""

# importing required libraries and modules
from __future__ import print_function
import tweepy

#function to search the hashtag phrase
def search_the_hashtag_phrase(consumer_api_key, consumer_api_secret_key, access_token \
                              , access_token_secret, hashtag):
    """
    Takes the input consumer key, consumer secret, access token, access
    token secret and hashtag for authorization to access twitter data
    and simply return the tweets associated with the following hashtag.
    """

    #creating authentication required for twitter API access
    auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    #getting each tweet that matches the following hashtag
    for each_tweet in tweepy.Cursor(api.search, q = hashtag + ' -filter:retweets',\
                                    lang = 'en', tweet_mode = 'extended').items(2):
        print(each_tweet)

consumer_api_key = raw_input('Enter your consumer api key :\n')
consumer_api_secret_key = raw_input('Enter your consumer api secret key :\n')
access_token = raw_input('Enter your access token :\n')
access_token_secret = raw_input('Enter your access token secret :\n')
hashtag = raw_input('Enter the hashtag from which you want to pull tweets :\n')

if __name__ == '__main__':
    search_the_hashtag_phrase(consumer_api_key, consumer_api_secret_key, access_token \
                              , access_token_secret, hashtag)
