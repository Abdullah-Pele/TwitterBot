import tweepy
import time

import tweepy
import time


def pages_taker(ap, method , number, target_name, sec=10):
    pages = []
    for x in tweepy.Cursor(method, screen_name=target_name).pages(number):
        pages.extend(x)
        time.sleep(sec)
    # print(pages)
    # print(len(pages))
    return pages

def follow_followers(ap, seconds, number, target_name):
    pages_number = (number+5000)//5000
    pages = pages_taker(ap, ap.followers_ids, pages_number, target_name)
    counter = 0
    for x in pages:
        if not ap.show_friendship( target_id=x)[0].following:
            try:
                ap.create_friendship(x)
                counter += 1
                print("screen name: "+ap.get_user(x).screen_name+" Follow number ="+str(counter))
                if counter > number:
                    return counter
                    break
                time.sleep(seconds)
            except tweepy.error.TweepError as e:
                print(e)

def follow_friends(ap, seconds, number, target_name):
    pages_number = (number+5000)//5000
    pages = pages_taker(ap, ap.friends_ids, pages_number, target_name)
    counter = 0
    for x in pages:
        try:
            if not ap.show_friendship( target_id=x)[0].following:
                ap.create_friendship(x)
                counter += 1
                print("screen name: "+ap.get_user(x).screen_name+" Follow number ="+str(counter))
                if counter > number:
                    return counter
                    break
                time.sleep(seconds)

        except tweepy.error.TweepError as e:
                print(e)

def unfollow_friends(ap, seconds, number, target_name=""):
    pages_number = (number+5000)//5000
    pages = pages_taker(ap, ap.friends_ids, pages_number, target_name)
    counter = 0
    for x in pages:
        try:
            ap.destroy_friendship(x)
            counter += 1
            print("screen name: "+ap.get_user(x).screen_name+" UnFollow number ="+str(counter))
            if counter > number:
                return counter
                break
            time.sleep(seconds)
        except tweepy.error.TweepError as e:
                print(e)

def unfollow_followers(ap, seconds, number, target_name=""):
    pages_number = (number+5000)//5000
    pages = pages_taker(ap, ap.followers_ids, pages_number, target_name)
    counter = 0
    for x in pages:
        try:
            ap.destroy_friendship(x)
            counter += 1
            print("screen name: "+ap.get_user(x).screen_name+" UnFollow number ="+str(counter))
            if counter > number:
                return counter
                break
            time.sleep(seconds)
        except tweepy.error.TweepError as e:
                print(e)


def unfollow_enemies(ap, seconds, number, target_name):
    pages_number = (number+5000)//5000
    pages = pages_taker(ap, ap.friends_ids, pages_number, target_name)
    counter = 0
    for x in pages:
        try:
            if not ap.show_friendship( target_id=x)[0].followed_by:
                ap.destroy_friendship(x)
                counter += 1
                print("screen name: "+ap.get_user(x).screen_name+" UnFollow number ="+str(counter))
                if counter > number:
                    return counter
                    break
                time.sleep(seconds)
        except tweepy.error.TweepError as e:
                print(e)

def pages_taker(ap, method , number, target_name, sec=60):
    pages = []
    for x in tweepy.Cursor(method, screen_name=target_name).pages(number):
        pages.extend(x)
        time.sleep(sec)
    # print(pages)
    # print(len(pages))
    return pages

def follow_followers(ap, seconds, number, target_name):
    pages_number = (number+5000)//5000
    pages = pages_taker(ap, ap.followers_ids, pages_number, target_name)
    counter = 0
    for x in pages:
        if not ap.show_friendship( target_id=x)[0].following:
            try:
                api.create_friendship(x)
                counter += 1
                print("screen name: "+ap.get_user(x).screen_name+" Follow number ="+str(counter))
                if counter > number:
                    break
                time.sleep(seconds)
            except tweepy.error.TweepError as e:
                print(e)

def follow_friends(ap, seconds, number, target_name):
    pages_number = (number+5000)//5000
    pages = pages_taker(ap, ap.friends_ids, pages_number, target_name)
    counter = 0
    for x in pages:
        try:
            if not ap.show_friendship( target_id=x)[0].following:
                api.create_friendship(x)
                counter += 1
                print("screen name: "+ap.get_user(x).screen_name+" Follow number ="+str(counter))
                if counter > number:
                    break
                time.sleep(seconds)

        except tweepy.error.TweepError as e:
                print(e)

def unfollow_friends(ap, seconds, number, target_name=""):
    pages_number = (number+5000)//5000
    pages = pages_taker(ap, ap.friends_ids, pages_number, target_name)
    counter = 0
    for x in pages:
        try:
            api.destroy_friendship(x)
            counter += 1
            print("screen name: "+ap.get_user(x).screen_name+" UnFollow number ="+str(counter))
            if counter > number:
                break
            time.sleep(seconds)
        except tweepy.error.TweepError as e:
                print(e)

def unfollow_enemies(ap, seconds, number):
    pages_number = (number+5000)//5000
    pages = pages_taker(ap, ap.friends_ids, pages_number,"")
    counter = 0
    for x in pages:
        try:
            if not ap.show_friendship( target_id=x)[0].followed_by:
                api.destroy_friendship(x)
                counter += 1
                print("screen name: "+ap.get_user(x).screen_name+" UnFollow number ="+str(counter))
                if counter > number:
                    break
                time.sleep(seconds)
        except tweepy.error.TweepError as e:
                print(e)


def follow_target_followers(ap, seconds, number, target_name):

    for x in tweepy.Cursor(ap.followers_ids, screen_name=target_name).items(number):
        try:
            api.create_friendship(x)
            print("id "+str(x)+" Follow")
            time.sleep(seconds)
        except tweepy.error.TweepError as e:
            print(e)


def follow_target_following(ap, seconds, number, target_name):

    for x in tweepy.Cursor(ap.friends_ids, screen_name=target_name).items(number):
        try:
            api.create_friendship(x)
            print("id "+str(x)+" Follow")
            time.sleep(seconds)
        except tweepy.error.TweepError as e:
            print(e)
def unfollow_my_freinds(ap, seconds, number, target_name=""):
    for x in tweepy.Cursor(ap.friends_ids, screen_name=target_name).items(number):
        try:
            ap.destroy_friendship(x)
            print("id "+str(x)+" UNFollow")
            time.sleep(seconds)
        except tweepy.error.TweepError as e:
            print(e)

def unfollow_not_friends(ap, seconds,number,target_name=""):

    followers = ap.followers_ids(target_name)
    friends = ap.friends_ids(target_name)

    for f in friends[:number]:
        if f not in followers:
            print ("Unfollow {0}?".format(api.get_user(f).screen_name))
            ap.destroy_friendship(f)
            time.sleep(seconds)

screen_name = ""
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

#just a test
#follow_followers(api, 1, 10, "al_eneziii")
