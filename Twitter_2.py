import tweepy
from tweepy import OAuthHandler
from Lab2 import Credentials
import json
from nltk.tokenize import word_tokenize
import re


#Obtain credentials for accessing the application
auth = OAuthHandler(Credentials.consumer_key, Credentials.consumer_secret)
auth.set_access_token(Credentials.access_token, Credentials.access_secret)

#Call Twitter Auth
api = tweepy.API(auth)

#Obtain user
user = api.me()


#####################################################

#Get three tweets
print('\n\nTimeline: ')
# we use 1 to limit the number of tweets we are reading
# and we only access the `text` of the tweet
listStatus = tweepy.Cursor(api.home_timeline).items(10)
for status in listStatus:
    print(status.text)



#Get JSON format
#print('\n\nJSON example: \n')
#for friend in tweepy.Cursor(api.friends).items(1):
#   print(json.dumps(friend._json, indent=2))


#Search tweets
#for tweet in tweepy.Cursor(api.search, q = "google", since = "2014-02-14", until = "2014-02-15", lang = "en").items(10):
#    print(tweet.text)




###################
#### TOKENIZER ####
###################


#Emoticon expresion
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

#Char strings
regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


#Search 3 tweets and tokenize it
print("\n\n")
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(preprocess(status.text))





