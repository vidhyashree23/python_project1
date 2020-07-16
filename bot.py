import tweepy
import time

consumer_key = '2z4UPRe3Lk16YfmHleEp1TzdZ'
consumer_secret = 'T6kq8MSK4pBzfFYOyI9MqNd3rphlvTuD1J6Bq6kCP140dkBvfu'
key = '876819947246149632-jlJDCDDHr01FCPwFOzqBzJ0Pb0R0vLN'
secret = '69rtYzW0ODf6Pxsaj752Ldq1kEC5owLC0OmvAbYbGOKHr'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)



FILE_NAME = "last_seen.txt"
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME,"r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME,last_seen_id):
    file_write = open(FILE_NAME,"w")
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode ='extended')
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("replied to tweet"  + str(tweet.id))
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            api.update_status("@" + tweet.user.screen_name +  " GOOD LUCK",tweet.id)
            store_last_seen(FILE_NAME,tweet.id)
while True:
    reply()
    time.sleep(15)
