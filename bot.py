import os
import praw
import random
import time
# import pprint
# import pandas as pd
# df = pd.DataFrame()

from dotenv import load_dotenv
load_dotenv()

from gpt import gptResponse
# from utils import getProperties

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
)

# GRAB A "RANDOM" POST FROM ELIF
# "RAMDOM" = ONE RANDOMLY SELECTED *RECENT* POST THAT *DOES NOT* HAVE SELFTEXT PROPERTY
# GENERATE GPT RESPONSE TO POST AND REPLY WITH GENERATED RESPONSE
# REPEAT EVERY HOUR

def grabPost(subreddit_string):
    subreddit = reddit.subreddit(subreddit_string)
    for post in subreddit.new(limit=10):
        if post.selftext == '':
            return post

def bot():
    post = grabPost('explainlikeimfive')
    print(post.title)
    gpt_response = gptResponse(post.title)
    print(gpt_response)
    # post.reply(gpt_response)

while True:
    bot()
    time.sleep(3600)





