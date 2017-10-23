
# coding: utf-8

# In[6]:

import tweepy
import pandas as pd
from config import config


# In[19]:

usernames = ''
usernames = pd.read_csv('users.csv')


# In[21]:

lines = []
for handle in usernames['Users']:
    lines.append(handle)

if(config == None):
    print "Mount a config.py file into the container"
    quit()

print "Read captains list: " + str(len(lines))

auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_token"], config["access_token_secret"])

api = tweepy.API(auth)

me = api.me()
users = lines

# Backwards-compatibility with v0.1 of program.
if "appear_in_my_feed" not in config:
    config["appear_in_my_feed"] = True

for user in users:
    try:
        status = api.show_friendship(target_screen_name = user)
        if(status[0].screen_name != status[1].screen_name):
            if(status[0].following == False):
                api.create_friendship(screen_name = status[1].screen_name, follow = config["appear_in_my_feed"])
                print("Following: " + status[1].screen_name)
            else:
                print("Already Following " +status[1].screen_name)
    except tweepy.TweepError as e:
            print(e)
            continue


# In[ ]:



