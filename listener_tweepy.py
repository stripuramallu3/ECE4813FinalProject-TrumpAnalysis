#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer,KafkaClient 
#Get Twitter API keys from Twitter developer account
access_token = "772234465057931264-OWIX3wDgn3r77wdN0Y1UM95rKGALc1D"
access_token_secret = "GqGZNoVZO8RuODsU7wFI7jhSJtui3ooJRDQ7d32iS1Coh"
consumer_secret = "gAwD1X8XdNwnl2X11TsZmYay3b9jFcvP5hQNlbLJVZBIw1Vbgb"
consumer_key = "yWCC61dsZVHFkYsucAGCJJa5o"



#Implement this function to publish data to Kafka topic
#def publish:

 #   return True    
    
    
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        producer.send_messages("forestfire",data.encode('utf-8'))
        print(data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    print 'Listening...'
    #This handles Twitter authetification and the connection to Twitter Streaming API
    client = KafkaClient('ip-172-31-88-122.ec2.internal:6667')
    producer = SimpleProducer(client)
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['trump'])
