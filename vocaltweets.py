import tweepy
import webbrowser
import time
from excelextracts import final_list
import random



consumer_key = "CONSUMERKEY"
consumer_secret = "CONSUMERSECRET"

callback_uri = 'oob'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)

webbrowser.open(redirect_url)

user_pin_input = input('what is the pin? ')

auth.get_access_token(user_pin_input)
api = tweepy.API(auth)


for tweet in final_list:
    new_status = api.update_status(tweet)
    time.sleep(random.randrange(10,100))

