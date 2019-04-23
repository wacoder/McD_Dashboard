# coding=utf-8

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient
import secrets
import json

access_token = secrets.access_token
access_token_secret = secrets.access_secret_token

consumer_key = secrets.consumer_key
consumer_secret = secrets.consumer_secret_key


class StdOutListener(StreamListener):
    def on_status(self, status):
        data = status._json
        text = data['text'].encode('utf-8')
        text = str(text).lower()
        
        if data.get('place',{}).get('country') == 'Canada':
            print(text)

        # for key, value in data.items():
        #     print(key)
            
        return True
    def on_err(self, status):
        print(status)

l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.filter(locations=[ -132.678892, 38.254429,-50.950142,62.091894])
