import pandas as pd
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt

r_key = "UZsGlNd58jFSnkbzmiIj0asIH"
consumer_key_secret = "cdv0HfYrqJ7517qXQnDy7y24oaHLbmZ2z2l2ZFECzS5EwylSEG"
access_token = "1452533975180738562-iDShopCCVrvtIwlTgUzP94UHJIyjYV"
access_token_secret = "N1807EGuy1F5bCMZEreYpQfsVdiEQ7ABjpQfvMxZNOxPq"
auth = tweepy .OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit= True)

def cleanText(text):
    text = re.sub(r"@[A-Za-z0-9]+", '', text) #removed @mentions
    text = re.sub(r'#', '', text) #removing # symbol
    text = re.sub(r'RT[\s]+', '', text) #removing retweets RT
    text = re.sub(r'https?:\/\/\S+', '', text) #removes the hyperlink

    return text

def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity

def getAnalysis(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"

def get_keyword_tweets(keyword, count):
    items = api.search_30_day(label='development', query=keyword, maxResults= count)
    return items

test_list = get_keyword_tweets("infosys",15)
#test_list[0]._json["text"]

df = pd.DataFrame({"tweet": [tweet.text for tweet in test_list], "language":[tweet.lang for tweet in test_list],"likes": [tweet.favorite_count for tweet in test_list],"retweets": [tweet.retweet_count for tweet in test_list]})