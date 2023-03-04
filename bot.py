import os
import praw
import random
import time
import pprint
# import pandas as pd
# df = pd.DataFrame()

from dotenv import load_dotenv
load_dotenv()

from gpt import gptResponse
# from utils import getProperties

reddit = praw.Reddit(
    client_id=os.getenv('RF_CLIENT_ID'),
    client_secret=os.getenv('RF_CLIENT_SECRET'),
    user_agent=os.getenv('RF_USER_AGENT'),
    username=os.getenv('RF_USERNAME'),
    password=os.getenv('RF_PASSWORD')
)

# REGINALD FRANZEN
# GRAB A "RANDOM" POST FROM ELIF
# "RAMDOM" = ONE RANDOMLY SELECTED *RECENT* POST THAT *DOES NOT* HAVE SELFTEXT PROPERTY
# GENERATE GPT RESPONSE TO POST AND REPLY WITH GENERATED RESPONSE
# REPEAT EVERY HOUR

def grabELIFPost():
    subreddit = reddit.subreddit('explainlikeimfive')
    for post in subreddit.new(limit=10):
        if post.selftext == '':
            return post

def reggieFranzen():
    ELIF_post = grabELIFPost()
    ELIF_post.upvote()
    print(ELIF_post.title)
    GPT_response = gptResponse(ELIF_post.title)
    print(GPT_response)
    ELIF_post.reply(GPT_response)


## BETTE QUIGLEY
## RESPOND TO WRITING PROMPTS? IDK

def betteQuigley():
    print('chello')


reggieFranzen()



# while True:
#     reggieFranzen()
#     time.sleep(21600)





