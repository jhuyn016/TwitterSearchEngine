import tweepy
from tweepy import OAuthHandler
import os

def authenticate():
    consumer_key = '5phTamiIP8B6rIizoUmBFjV4v'
    consumer_secret = '4HfI4O6HHix1inuXhof8aN2au0GKBdpQhZrZjc8u5lLxuvyDy1'
    access_token = '904501601146101762-tklO2ZF65vRShtHxNC0nhV0a7wGbtBg'
    access_secret = 'kq2WpalEuDexL9Zm7bfWHpW9I10yFgnYUmLJvK7dtRcv7'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth
	
