# TweetAnalyzer.py will stream positive tweets on a keyword or handle
# Usage: in a commandline: python tweetanalyzer.py keyword
# No need to use an @ for a handle
#
#
#


#Import the necessary methods from tweepy library
import json
import re
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

#Get Twitter API keys from Twitter developer account
access_token = "19559894-tvL69XC7oR4Y3BxwK35W652C0FLPhit3oO6rIVD0V"
access_token_secret = "mUYU6tLGgiUaIqj5Mt69RqoWgkmAmXv7sDPU853OCWCs4"
consumer_key = "P1Yn4XDNnTh0Ocgz1M9RbQRVj"
consumer_secret = "9amzFy5mU5gsDlXxQCkMbTn8T0hwJ8SIbn5QMR3BcONONifYsd"

TERMS={}

#-------- Load Sentiments Dict ----
sent_file = open('AFINN-111.txt')
sent_lines = sent_file.readlines()
for line in sent_lines:
	s = line.split("\t")
	TERMS[s[0]] = s[1]

sent_file.close()   

def analyzeData(data):
    sentiment = 0.0
    
    text = data	
    text=re.sub('[!@#$)(*<>=+/:;&^%#|\{},.?~`]', '', text)
    splitTweet=text.split()

    for word in splitTweet:
        if TERMS.has_key(word):
            sentiment = sentiment+ float(TERMS[word])
    return sentiment

class StdOutListener(StreamListener):

    def on_data(self, data):
        data_json = json.loads(data)
        user = data_json['user']['screen_name']
        tweet_text = data_json['text']
        tweet_id = data_json['id_str']
        sentiment = analyzeData(tweet_text)
        if sentiment > 1.0:
            print ('Twitter Handle ' + user + ' said: ' + tweet_text + 
                '   link: ' + 'http://twitter.com/' + user + '/status/' + tweet_id)
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
	brand = sys.argv[1]
	print ('Listening for positive tweets on ' + brand + '...')
	
#This will authorize our listener
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
#This will set the stream and look for the keyword 	
	stream = Stream(auth, l)
	stream.filter(track=[brand])