#!/usr/bin/env python
from secrets import *
from twython import TwythonStreamer
import train
train.main()
from colorama import init, Fore, Back 
train.categories[0].colour = Fore.GREEN + Back.BLACK
train.categories[1].colour = Fore.RED + Back.WHITE
reset = Fore.RESET + Back.RESET

class SentimentStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            mood = train.classify(data['text'])
            if mood is None:
                print data['text'].encode('utf-8')
                print "neutral"
            else: 
                print mood.colour + data['text'].encode('utf-8') + reset
                print(mood)

    def on_error(self, status_code, data):
        print status_code

stream = SentimentStreamer(APP_KEY, APP_SECRET, 
           OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(locations=[-6.833496, 49.894634, 2.087402, 59.623325])

