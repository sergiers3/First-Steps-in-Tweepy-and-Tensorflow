import tweepy
from tweepy import OAuthHandler
from Lab2 import Credentials
from Lab2 import Access

#Consumer credentials
consumer_key = Credentials.consumer_key
consumer_secret = Credentials.consumer_secret

#Instance Access object and follow the PIN process
access = Access.obj

#Get the Access Token and the Secret Token from the access OBJ
at = access.atk
ase = access.ats

#Auth as allways with the secret tokens obtained from twitter
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(Credentials.access_token, Credentials.access_secret)

api = tweepy.API(auth)
user = api.me()

#Print some data
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.followers_count))
print('Created: ' + str(user.created_at))
print('Description: ' + str(user.description))


