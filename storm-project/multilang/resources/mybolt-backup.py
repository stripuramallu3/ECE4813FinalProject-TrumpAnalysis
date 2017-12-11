import storm
import datetime
import time
import boto3
import re
import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#Enter AWS Credentials
ACCESS_KEY="" 
SECRET_KEY=""
REGION=""

# Get the table
dynamodb = boto3.resource('dynamodb', aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_KEY,
                            region_name=REGION)
table = dynamodb.Table('tweetsentiment')

#Load Sentiment Dictionary
TERMS={}
nltk.download('vader_lexicon')
#-------- Load Sentiments Dict ----
sent_file = open('AFINN-111.txt')
sent_lines = sent_file.readlines()
for line in sent_lines:
	s = line.split("\t")
	TERMS[s[0]] = s[1]

sent_file.close()


def analyzeData(tweet):
    sentiment=0.0
  #  tweet = tweet.encode('utf-8')
  #  tweet = json.loads(tweet) 
    if tweet.has_key('text'):
	sid = SentimentIntensityAnalyzer()
        text = tweet['text']		
        text=re.sub('[!@#$)(*<>=+/:;&^%#|\{},.?~`]', '', text)
       	'''
	 splitTweet=text.split()
	
        for word in splitTweet:
            if TERMS.has_key(word):
                sentiment = sentiment+ float(TERMS[word])
	'''
    	sentiment = sid.polarity_scores(text)
    	#sentiment = str(sentiment["compound"])
    return str(0.0)
    #Add your code for data analysis here

class MyBolt(storm.BasicBolt):
    def process(self, tup):
        data = tup.values[0]
        data = json.loads(data)
        sentiment = analyzeData(data)
       
        ts=time.time()
       # timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        table.put_item(
            Item={
                "timestamp": str(ts),
                "data": data['text'],
                "prediction": "0"
                 }
        ) 
        storm.emit([result])

MyBolt().run()

