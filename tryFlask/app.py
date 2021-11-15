from bokeh.models.annotations import Label
from flask import Flask
from flask import request
from flask import render_template,jsonify
from bokeh.embed import components
from bokeh.plotting import figure
import pandas as pd
import numpy as np
import datetime
import pickle
from bokeh.plotting import figure, output_file, show
from bokeh.transform import dodge, linear_cmap
from bokeh.util.hex import hexbin
import json

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():

    if request.method == 'GET':
        allStock = pd.read_csv('NIFTY50_all.csv')
        stock_symbols=allStock.Symbol.unique()
        table = pd.read_csv('hdfc2.csv')
        table1 = pd.read_csv('hdfc2.csv')
        my_data = DataSaved3(table)
        my_data1 = DataSaved3(table1)
        labels=[]
        for i in my_data['labs']:
            labels.append(str(i))
        PosVal = my_data['val_1']
        NeuVal = my_data['val_2']
        NegVal = my_data['val_3']
        PosPlot = json.dumps(my_data['PosPlot'])
        NegPlot = json.dumps(my_data['NegPlot'])
        NeuPlot = json.dumps(my_data['NeuPlot'])
        labels1=[]
        for i in my_data1['labs']:
            labels1.append(str(i))
        PosVal1 = my_data1['val_1']
        NeuVal1 = my_data1['val_2']
        NegVal1 = my_data1['val_3']
        kwargs ={'PosVal':PosVal,'NeuVal':NeuVal,'NegVal':NegVal, 'NegPlot':NegPlot, 
        'NeuPlot':NeuPlot, 'PosPlot':PosPlot,'labels':labels,'PosVal1':PosVal1,
        'NeuVal1':NeuVal1,'NegVal1':NegVal1,'labels1':labels1}
        kwargs['title'] = 'homepage'
        return render_template('graph.html', **kwargs, stock_symbols=stock_symbols)
    else:
        return render_template('graph.html')

@app.route('/data')
def data():
    return jsonify({'results':[10,20,30,40,50]})

@app.route('/details/<st_name>')
def details(st_name):
    if(st_name == '1'):
        tb = pd.read_csv('tata.csv')
    else:
        tb = pd.read_csv('hdfc2.csv')
    my_data = DataSaved3(tb)
    labels=[]
    for i in my_data['labs']:
        labels.append(str(i))
    PosVal = my_data['val_1']
    NeuVal = my_data['val_2']
    NegVal = my_data['val_3']
    PosPlot = json.dumps(my_data['PosPlot'])
    NegPlot = json.dumps(my_data['NegPlot'])
    NeuPlot = json.dumps(my_data['NeuPlot'])

    kwargs ={'PosVal':PosVal,'NeuVal':NeuVal,'NegVal':NegVal, 'NegPlot':NegPlot, 
        'NeuPlot':NeuPlot, 'PosPlot':PosPlot,'labels':labels}
    return render_template('details.html', **kwargs)

@app.route("/dropSel", methods=['GET', 'POST'])
def dropSel():
    if(request.method =='POST'):
        tb=pd.read_csv(request.form['DDst'])
        print(request.form['DDst'])
        my_data = DataSaved3(tb)
        labels=[]
        for i in my_data['labs']:
            labels.append(str(i))
        PosVal = my_data['val_1']
        NeuVal = my_data['val_2']
        NegVal = my_data['val_3']
        PosPlot = json.dumps(my_data['PosPlot'])
        NegPlot = json.dumps(my_data['NegPlot'])
        NeuPlot = json.dumps(my_data['NeuPlot'])

        kwargs ={'PosVal':PosVal,'NeuVal':NeuVal,'NegVal':NegVal, 'NegPlot':NegPlot, 
            'NeuPlot':NeuPlot, 'PosPlot':PosPlot,'labels':labels}
        return render_template('details.html', **kwargs)

@app.route('/',methods = ['GET','POST'])
def index1():
    table = pd.read_csv('NIFTY50_all.csv')
    stock_symbols = table.Symbol.unique()

    if request.method == 'GET':
        p = figure(width=200, height=250,sizing_mode="stretch_width")
        p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
        demo_script_code,chart_code1 = components(p)
        return render_template('Try.html',stock_symbol_names='stock_symbols', chart_code1 = chart_code1, demo_script_code1 = demo_script_code)
        # return render_template('Try.html')
    else:

        return render_template('Try.html')




@app.route('/MIndia')
def MIndia():
    tb = pd.read_csv('3m.csv')
    my_data = DataSaved3(tb)
    p = figure(plot_width = 650, plot_height = 350)
    p.vbar(x = dodge('labs', -0.25, range = p.x_range), top = 'val_1',legend_label="Positive",
    width = 0.2,source = my_data, color = "green")
    p.vbar(x = dodge('labs', 0.0, range = p.x_range), top = 'val_2',legend_label="Neutral",
    width = 0.2, source = my_data,color = "cyan")
    p.vbar(x = dodge('labs', 0.25, range = p.x_range), top = 'val_3',legend_label="Negative",
    width = 0.2,source = my_data,color = "blue")
    demo_script_code,chart_code = components(p)
    kwargs = {'chart_code': chart_code, 'demo_script_code': demo_script_code}
    kwargs['title'] = '3M India'
    return render_template('details.html',**kwargs)

@app.route('/Voltas')
def Voltas():
    tb = pd.read_csv('hdfc2.csv')
    my_data = DataSaved3(tb)
    p = figure(plot_width = 650, plot_height = 350)
    p.vbar(x = dodge('labs', -0.25, range = p.x_range), top = 'val_1', legend_label="Positive",
    width = 0.2,source = my_data, color = "green")
    p.vbar(x = dodge('labs', 0.0, range = p.x_range), top = 'val_2', legend_label="Neutral",
    width = 0.2, source = my_data,color = "cyan")
    p.vbar(x = dodge('labs', 0.25, range = p.x_range), top = 'val_3', legend_label="Negative",
    width = 0.2,source = my_data,color = "blue")
    demo_script_code,chart_code = components(p)
    kwargs = {'chart_code': chart_code, 'demo_script_code': demo_script_code}
    kwargs['title'] = 'HDFC'
    return render_template('details.html',**kwargs)

@app.route('/Bosch')
def Bosch():
    tb = pd.read_csv('bosch2.csv')
    my_data = DataSaved3(tb)
    p = figure(plot_width = 650, plot_height = 350)
    p.vbar(x = dodge('labs', -0.25, range = p.x_range), top = 'val_1',
    width = 0.2,source = my_data, color = "green")
    p.vbar(x = dodge('labs', 0.0, range = p.x_range), top = 'val_2',
    width = 0.2, source = my_data,color = "cyan")
    p.vbar(x = dodge('labs', 0.25, range = p.x_range), top = 'val_3',
    width = 0.2,source = my_data,color = "blue")
    demo_script_code,chart_code = components(p)
    kwargs = {'chart_code': chart_code, 'demo_script_code': demo_script_code}
    kwargs['title'] = 'Bosch'
    return render_template('details.html',**kwargs)

def DataSaved(table):
    import pandas as pd
    import tweepy
    from textblob import TextBlob
    from wordcloud import WordCloud
    import numpy as np
    import matplotlib.pyplot as plt
    import re
    Analysis = table['Analysis'].tolist()
    pos=neg=neu=0
    positive=[]
    negative=[]
    neutral=[]
    for i in range(0,len(Analysis)):
        if(i%20 == 0 and i!=0):
            positive.append(pos)
            neutral.append(neu)
            negative.append(neg)
        else:
            if(Analysis[i] == "Positive"):
                pos +=1
            elif(Analysis[i] == "Neutral"):
                neu +=1
            else:
                neg +=1
    labs=[]
    for i in range(0,49):
        labs.append(i)
    my_data = {'labs':labs,
    'val_1':positive,
    'val_2':neutral,
    'val_3':negative
    }
    print(my_data['labs'])
    return  my_data

def DataSaved3(table):
    import pandas as pd
    import tweepy
    from textblob import TextBlob
    from wordcloud import WordCloud
    import numpy as np
    import matplotlib.pyplot as plt
    import re
    Analysis = table['Analysis'].tolist()
    tweet = table['tweet'].tolist()
    pos=neg=neu=0
    positive=[]
    negative=[]
    neutral=[]
    tempPos=[]
    tempNeg=[]
    tempNeu=[]
    PosReview=[]
    NeuReview=[]
    NegReview=[]
    for i in range(0,len(Analysis)):
        if(i%10 == 0 and i!=0):
            positive.append(pos)
            neutral.append(neu)
            negative.append(neg)
            pos=neg=neu=0
            PosReview.append(tempPos)
            NeuReview.append(tempNeu)
            NegReview.append(tempNeg)
            tempPos = []
            tempNeu = []
            tempNeg = []
        if(Analysis[i] == "Positive"):
            pos +=1
            tempPos.append(tweet[i])
        elif(Analysis[i] == "Neutral"):
            neu +=1
            tempNeu.append(tweet[i])
        else:
            neg +=1
        tempNeg.append(tweet[i])
    
    PosPlot=[]
    for i in range(0,len(PosReview)):
        x = {}
        x['nums'] = i
        x['prod'] = {'val':positive[i],'link':PosReview[i]}
        PosPlot.append(x)

    NegPlot=[]
    for i in range(0,len(PosReview)):
        x ={}
        x['nums'] = i
        x['prod'] = {'val':negative[i],'link':NegReview[i]}
        NegPlot.append(x)
    
    NeuPlot=[]
    for i in range(0,len(PosReview)):
        x ={}
        x['nums'] = i
        x['prod'] = {'val':neutral[i],'link':NeuReview[i]}
        NeuPlot.append(x)

    labs=[]
    for i in range(0,8):
        labs.append(i)
    my_data = {'labs':labs,
    'val_1':positive,
    'val_2':neutral,
    'val_3':negative,
    'NeuPlot':NeuPlot,
    'NegPlot':NegPlot,
    'PosPlot':PosPlot
    }
    return  my_data

def DataSaved1(table):
    import pandas as pd
    import tweepy
    from textblob import TextBlob
    from wordcloud import WordCloud
    import numpy as np
    import matplotlib.pyplot as plt
    import re
    Analysis = table['Analysis'].tolist()
    pos=neg=neu=0
    positive=[]
    negative=[]
    neutral=[]
    for i in range(0,len(Analysis)):
        if(i%20 == 0 and i!=0):
            positive.append(pos)
            neutral.append(neu)
            negative.append(neg)
            pos=neg=neu=0
        else:
            if(Analysis[i] == "Positive"):
                pos +=1
            elif(Analysis[i] == "Neutral"):
                neu +=1
            else:
                neg +=1
    labs=[]
    for i in range(0,20):
        labs.append(i)
    my_data = {'labs':labs,
    'val_1':positive,
    'val_2':neutral,
    'val_3':negative
    }
    return  my_data


def compute(Stname):
    import pandas as pd
    import tweepy
    from textblob import TextBlob
    from wordcloud import WordCloud
    import numpy as np
    import matplotlib.pyplot as plt
    import re

    consumer_key = "UZsGlNd58jFSnkbzmiIj0asIH"
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

    frames = []
    for i in range(10):
        frames.append(get_keyword_tweets(Stname,100))

    frames2 =[]
    for test_l in frames:
        df = pd.DataFrame({"tweet": [tweet.text for tweet in test_l], "language":[tweet.lang for tweet in test_l],"likes": [tweet.favorite_count for tweet in test_l],"retweets": [tweet.retweet_count for tweet in test_l]})
        frames2.append(df)

    big_table = pd.concat(frames2)
    big_table['tweet'] = big_table['tweet'].apply(cleanText)
    big_table["Subjectivity"] = big_table["tweet"].apply(getSubjectivity)
    big_table["Polarity"] = big_table["tweet"].apply(getPolarity)

    big_table["Analysis"] = big_table["Polarity"].apply(getAnalysis)

    # weet = test_list[1]
    # print(weet.created_at)

    # converting into list
    k =big_table['Analysis'].tolist()

    # storing all pos, neg, neu in type of list
    pos = neu = neg = 0
    positive=[]
    negative=[]
    neutral=[]
    for i in range(0,1000):
        if(i%50 == 0):
            positive.append(pos)
            negative.append(neg)
            neutral.append(neu)
            pos = neu = neg = 0
        else:
            if(k[i] == "Positive"):
                pos +=1
            elif(k[i] == "Neutral"):
                neg +=1
            else:
                neu +=1

    # graph making
    labs=[]
    for i in range(0,20):
        labs.append(i)
    my_data = {'labs':labs,
    'val_1':positive,
    'val_2':neutral,
    'val_3':negative
    }
    return(my_data)


if __name__ == '__main__':
    app.run(debug=True)