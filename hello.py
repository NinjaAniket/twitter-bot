import tweepy
import time


# get your credentials  key from twitter  developer account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
user = api.me()
print(user.followers_count)

### timelines from twitter account ##
# public_tweets = api.home_timeline()
# `for tweet in public_tweets:
#     print(tweet.text)


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = 'sushant singh rajput'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        # tweet.favorite() like a person's post with a keyword search_string
        tweet.retweet()
        print('thats cool')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
