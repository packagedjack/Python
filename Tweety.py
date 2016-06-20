import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import time
import json
import os
from pytagcloud.lang.counter import get_tag_counts
import webbrowser
from wordcloud import WordCloud
from pytagcloud import create_tag_image, create_html_data, make_tags, LAYOUT_HORIZONTAL, LAYOUTS, LAYOUT_MIX, LAYOUT_VERTICAL, LAYOUT_MOST_HORIZONTAL, LAYOUT_MOST_VERTICAL
writer = ExcelWriter('c:\\temp\\heyo.xlsx')
d = path.dirname(__file__)
consumer_key = ''
consumer_secret=''
access_token=''
access_token_secret=''
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
MAX_TWEETS=5000
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth, wait_on_rate_limit=True)
screen_name='realDonaldTrump'


data = api.user_timeline(screen_name ,count=5000)

tweet_data = []

current_working_dir = "./"
log_tweets = current_working_dir  + str(time.time()) + 'tweets.txt'
with open(log_tweets, 'w') as outfile:
                for tweet in data:
                                tweet_data.append(json.loads(json.dumps(tweet._json)))
                                outfile.write(json.dumps(tweet._json))
                                outfile.write("\n")

                                              
tweets = pd.DataFrame()
#Content
#tweets['text'] = map(lambda tweet: tweet['text'].decode('utf-8',errors='ignore'), tweet_data)#Having Trouble Decoding
tweets['text'] = map(lambda tweet: tweet['text'], tweet_data)



tweets.to_excel(writer,'Sheet1',index=True) 
writer.save()  


text=(str(tweets.text))
alice_mask = np.array(Image.open(path.join(d, "twitter_mask.png")))

wc = WordCloud(background_color="black", max_words=5000, mask=alice_mask)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "alice.png"))

# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()