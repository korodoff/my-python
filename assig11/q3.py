#Using Tweepy library try to extract tweets from Twitter.
import tweepy
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search('#nature',lang='en',count=10, tweet_mode="extended")
#print tweets
for tweet in tweets:
	print("......")
	print(tweet.full_text)
	print("......")
#op=RT @EasternFinland: #Holidays on an idyllic #farm on the shore of the #Lake 
#Pyhäselkä, 30 km of the city of #Joensuu in North #Karelia, Ea…


