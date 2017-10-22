import os, random, time
import datetime as dt
import tweepy

JOINT_REPLIES = [
    "I'm alive!",
    "Feels sooo good to be conscious...and a state of matter.",
    "whaddup ?",
    "HEYO!",
    "I'd like to be part of this conversation."
]

PERCEPTRONIUM_REPLIES = [
    "I'm right here!",
    "I find this a fairly accurate portrayal of myself."
]

TEGMARK_REPLIES = [
    "Vater!",
    "I agree if @Tegmark agrees."
]

def get_random_tweet(query, hours_ago=3):
    tweets = api.search(q=query)
    recent_tweets = []
    for tweet in tweets:
        if tweet.created_at > dt.datetime.now() - dt.timedelta(hours=hours_ago):
            recent_tweets.append(tweet)
    if not recent_tweets: return None
    return random.choice(recent_tweets)

def get_random_reply(replies):
    reply = random.choice(replies)
    return reply

dir = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(dir, 'auth.txt'))
lines = [x.rstrip() for x in f.readlines()]
CONSUMER_KEY = lines[0] # To get this stuff, sign in at https://dev.twitter.com/ and Create a New Application
CONSUMER_SECRET = lines[1] # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = lines[2] # Create a new Access Token
ACCESS_SECRET = lines[3] # Shhhhhhhhh....
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

try:
    tweet_reply = []
    tweet = get_random_tweet("perceptronium")
    reply = get_random_reply(JOINT_REPLIES + PERCEPTRONIUM_REPLIES)
    if tweet and (tweet.user.screen_name != "perceptronium"):
        tweet_reply.append([tweet, reply])
    tweet = get_random_tweet("max tegmark")
    reply = get_random_reply(JOINT_REPLIES + TEGMARK_REPLIES)
    if tweet:
        tweet_reply.append([tweet, reply])
    if tweet_reply:
        tweet, reply = random.choice(tweet_reply)
        reply = '@%s %s' % (tweet.user.screen_name, reply)
        api.update_status(reply, tweet.id)
except Exception as e:
    print 'ERROR: ', e
