# TweetAnalyzer

TweetAnalyzer.py will stream positive tweets that mention a handle. It uses a sentiment dictonary to analyze a tweet's text. The tweet is given a sentiment value, and only outputted if above 1 (for a positive tweet).

## Requirements
* Python
* Tweepy (to install, use pip install tweepy)
* AFINN-111.txt needs to be in the same folder level

## Usage
$ python tweetanalyzer.py handle
* No need to use an @ for a handle

### Example
$ python tweetanalyzer.py Microsoft