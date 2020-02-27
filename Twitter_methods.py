import tweepy
import time


f=open("log.txt", "a+")

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
                ap.create_friendship(x)
                counter += 1
                t= " "+time.asctime( time.localtime(time.time()) )+"\n"
                s= "screen name: "+ap.get_user(x).screen_name+" Follow number ="+str(counter)+t
                f.write(s)
                print(s)
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
                t = " "+time.asctime( time.localtime(time.time()) )+"\n"
                s= "screen name: "+ap.get_user(x).screen_name+" Follow number ="+str(counter)+t
                f.write(s)
                print(s)
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
            t = " "+time.asctime( time.localtime(time.time()) )+"\n"
            s= "screen name: "+ap.get_user(x).screen_name+" UnFollow number ="+str(counter)+t
            f.write(s)
            print(s)
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
            t = " "+time.asctime( time.localtime(time.time()) )+"\n"
            s= "screen name: "+ap.get_user(x).screen_name+" UnFollow number ="+str(counter)+t
            f.write(s)
            print(s)
            if counter > number:
                return counter
                break
            time.sleep(seconds)
        except tweepy.error.TweepError as e:
                print(e)


def unfollow_enemies(ap, seconds, number, target_name=""):
    pages_number = (number+5000)//5000
    pages = pages_taker(ap, ap.friends_ids, pages_number, target_name)
    counter = 0
    for x in pages:
        try:
            if not ap.show_friendship( target_id=x)[0].followed_by:
                ap.destroy_friendship(x)
                counter += 1
                t = " "+time.asctime( time.localtime(time.time()) )+"\n"
                s= "screen name: "+ap.get_user(x).screen_name+" UnFollow number ="+str(counter)+t
                f.write(s)
                print(s)
                if counter > number:
                    return counter
                    break
                time.sleep(seconds)
        except tweepy.error.TweepError as e:
                print(e)
