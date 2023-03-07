import os
import praw
import openai
import pprint
import random
import time
from gpt import gptResponse
from dotenv import load_dotenv

load_dotenv()
reddit_rf = praw.Reddit(
    client_id=os.getenv('RF_CLIENT_ID'),
    client_secret=os.getenv('RF_CLIENT_SECRET'),
    user_agent=os.getenv('RF_USER_AGENT'),
    username=os.getenv('RF_USERNAME'),
    password=os.getenv('RF_PASSWORD')
)

def likeXSubredditPosts(subreddits_array, number_of):
    selected = random.sample(subreddits_array, k=number_of)
    for subreddit in selected:
        print(f'IN SUBREDDIT "{subreddit}"')
        for post in subreddit.new(limit=1):
            # post.upvote()
            print(f'REGGIE FRANZEN HAS LIKED "{post.title}"')
            print('...')
            time.sleep(30)

def getSubreddits():
    list = []
    for this_subreddit in reddit_rf.user.subreddits(limit=None):
        list.append(this_subreddit)
    return list 






def ReggieFranzen():
    subreddits = getSubreddits()
    likeXSubredditPosts(subreddits, 5)
    # time.sleep(300)
    ## ENGAGE WITH ELIF
    # time.sleep(300)
    ## ENGAGE WITH ANOTHER SUB
    # time.sleep(300)
    ## AND SO ON???



ReggieFranzen()




# def main():
#     while True:
#         ReggieFranzen()