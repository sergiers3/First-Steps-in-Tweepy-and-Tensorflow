import tweepy
from tweepy import OAuthHandler
from Lab2 import Credentials


#Obtain credentials for accessing the application
auth = OAuthHandler(Credentials.consumer_key, Credentials.consumer_secret)
auth.set_access_token(Credentials.access_token, Credentials.access_secret)

#Call Twitter Auth
api = tweepy.API(auth)

#Obtain user
user = api.me()

#Print some data
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.followers_count))
print('Created: ' + str(user.created_at))
print('Description: ' + str(user.description))


