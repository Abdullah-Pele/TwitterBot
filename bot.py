import tweepy
# import time
# screen_name = "@twitter_acount_name"
#
import os
consumer_key = "put it here"
consumer_secret = "put it here"
#
access_token = "put it here"
access_token_secret = "put it here"
#
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# number_of_tweets = 1

#get tweets
tweets = api.user_timeline(screen_name = "@twitter_acount_name",count = 1)
print(tweets)

# with open("copy", "w") as file:
#     file.write("Your text goes here")
# fn = open('file.txt', "w")
# fn.write("hello am hidden")
# fn.close()
# print(fn.name)
# p = os.popen('attrib +h ' + fn.name)
# t = p.read()
# p.close()
# f = open("ttt","w")
# f.write("Hello World from " + f.name)    # Write inside file
# f.close()
# f = open("tmtmt", "w")
# f.write(consumer_key+"\n")
# f.write(consumer_secret+"\n")
# f.write(access_token+"\n")
# f.write(access_token_secret+"\n")
#
# f.close()
# print(api.me().name)
# api.update_status('Tweepy is here')

# user = api.me()
#
# print('Name: ' + user.name)
# print('Location: ' + user.location)
# print('Friends: ' + str(user.friends_count))

# for follower in tweepy.Cursor(api.followers).items():
#     follower.follow()

# followers = api.followers_ids("iMNI8pLAb4DF5qc")
# # friends = api.friends_ids()
# # print(followers)
#
# # follow the specefic sername followers
# for f in followers:
#     surnm = api.get_user(f)
#     api.create_friendship(surnm.id)
#     print("following : "+ surnm.screen_name)
