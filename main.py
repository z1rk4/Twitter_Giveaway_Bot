'''
Coded by Z1 :)

More features are underway! Email questions/concerns/feature requests 
at slitherthuglife@gmail.com or via twitter: @z1rk4

'''

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
import tweepy
import time
import datetime
import numpy as np
import config

found_tweets = []
measured_date = str(datetime.datetime.today())[0:8] + str(int(str(datetime.datetime.today())[8:10]) - 5)
TIME_SLEEP = 150 #Do not lower past 100, or you will get ratelimited
iterations = 0

def get_relevant_tweets(keyword, date):
    real_relevant_tweets = []
    recent_tweets = [tweet for tweet in tweepy.Cursor(api.search, q=keyword, since=date).items(5) if tweet not in found_tweets and tweet.text.lower()[0:4] != "rt @" and "congratulations" not in tweet.text.lower() and "congrats" not in tweet.text.lower()]

    for twt in recent_tweets:
        for kw in config.keywords:
            if kw in twt.text.lower():
                real_relevant_tweets.append(twt)
                
    return real_relevant_tweets

def get_tweets_from_user(twitter_handle):
    recent_tweets = [tweet for tweet in tweepy.Cursor(api.user_timeline, id=twitter_handle).items(5) if tweet not in found_tweets and tweet.text.lower()[0:4] != "rt @" and "giveaway" in tweet.text.lower() and "congratulations" not in tweet.text.lower() and "congrats" not in tweet.text.lower()]
    return recent_tweets

def retrieve_credentials(username):
    con_key = config.access_tokens[username]['consumer_key']
    con_secret = config.access_tokens[username]['consumer_secret']
    acc_token = config.access_tokens[username]['access_token']
    acc_token_scrt = config.access_tokens[username]['access_token_secret']

    return [con_key, con_secret, acc_token, acc_token_scrt]


if __name__ == "__main__":

    user_name = input("Enter your Twitter username: ")
    try:
        information = retrieve_credentials(user_name)

        consumer_key = information[0] 
        consumer_secret = information[1] 
        access_token = information[2]  
        access_token_secret = information[3] 

    except KeyError:
        print("\n\nCould not find credentials for '" + user_name + "'. Did you update access_tokens in config.py with correct credentials?\n\n")
        raise SystemExit

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    while True:
        measured_date = str(datetime.datetime.today())[0:8] + str(int(str(datetime.datetime.today())[8:10]) - 5)
        counter, follow_ct, like_ct, rt_ct, reply_ct = 0, 0, 0, 0, 0
        
        keyword_tweets = np.array([get_relevant_tweets(keywrd, measured_date) for keywrd in config.keywords])
        user_tweets = np.array([get_tweets_from_user(handle) for handle in config.account_names])
        
        filtered_keyword_tweets = []
        filtered_user_tweets = []
        
        for list_ in keyword_tweets:
            for twt in list_:
                filtered_keyword_tweets.append(twt)
                
        for list_ in user_tweets:
            for twt in list_:
                filtered_user_tweets.append(twt)
        
        filtered_keyword_tweets = np.array(filtered_keyword_tweets)
        filtered_user_tweets = np.array(filtered_user_tweets)
        
        total_tweets = np.concatenate((filtered_user_tweets, filtered_keyword_tweets))
        
        for tweet in total_tweets:
            reply = ""
            found_tweets.append(tweet)
            latest_tweet = tweet
            tweet_text = latest_tweet.text.lower()

            try:
                tweet.user.follow()
                
                screen_names = [mention["screen_name"] for mention in tweet.entities["user_mentions"]]
                for user in screen_names:
                    api.create_friendship(user)
                    follow_ct += 1
                
                follow_ct += 1

            except tweepy.TweepError:
                pass

            except StopIteration:
                break    


            if "retweet" in tweet_text or "rt" in tweet_text:
                try:
                    tweet.retweet()
                    rt_ct += 1

                except tweepy.TweepError:
                    pass

                except StopIteration:
                    break


            if "like" in tweet_text:
                try:
                    tweet.favorite()
                    like_ct += 1

                except tweepy.TweepError:
                    pass

                except StopIteration:
                    break

            if "tag 1" in tweet_text or "tag one" in tweet_text or "tag a" in tweet_text: 
                reply += "@" + config.tag_users[0] + " "

            if "tag 2" in tweet_text or "tag two" in tweet_text:
                reply += "@" + config.tag_users[0] + " "
                reply += "@" + config.tag_users[1] + " "

            if "tag 3" in tweet_text or "tag three" in tweet_text:
                reply += "@" + config.tag_users[0] + " "
                reply += "@" + config.tag_users[1] + " "
                reply += "@" + config.tag_users[2] + " "

            if len(config.trade_link) > 0 or len(config.wax_trade_link) > 0:
                for kw in config.link_paste_keywords:
                    if kw in tweet_text:
                        if "steam" in tweet_text:
                            reply += config.trade_link + " "
                        elif "wax" in tweet_text or "express" in tweet_text:
                            reply += config.link_paste_keywords + " "

            if len(config.datdrop_profile_link) > 0:
                if "datdrop" in tweet_text and "profile" in tweet_text:
                    reply += config.datdrop_profile_link + " "

            if len(config.custom_replies) > 0:
                for custom_keyword in config.custom_replies:
                    if custom_keyword.lower() in tweet_text:
                        reply += config.custom_replies[custom_keyword] + " "

            if len(reply) > 0:
                try:
                    reply_to_tweet = "@" + str(tweet.user.screen_name) + " " + reply
                    api.update_status(reply_to_tweet, in_reply_to_status_id = tweet.id)
                    reply_ct += 1
                    
                except tweepy.TweepError:
                    pass
                
                except StopIteration:
                    break

            counter += 1

        iterations += 1
        print(iterations, "iterations have passed,", counter, "new tweets found,", follow_ct, "new users followed,", like_ct, "new tweets liked,", rt_ct, "new tweets retweeted,", reply_ct, "new tweets replied to.")
        
        time.sleep(TIME_SLEEP)
    