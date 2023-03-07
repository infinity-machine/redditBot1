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

def respondToELIFPost():
    ELIF = reddit_rf.subreddit('explainlikeimfive')
    for post in ELIF.new(limit=10):
        # REPLY TO FIRST NEW POST THAT DOESN'T HAVE A SELFTEXT PROPERTY AND BREAK LOOP
        if (post.selftext == ''):
            rf_response = gptResponse(post.title)
            # post.reply(rf_response)
            print(f'REGGIE FRANZEN HAS RESPONDED TO {post.title}:')
            print(f'"{rf_response}" -- R.F.')
            return

def likeXSubredditPosts(subreddits_array, number_of):
    selected = random.sample(subreddits_array, k=number_of)
    for subreddit in selected:
        print(f'IN SUBREDDIT "{subreddit}"')
        for post in subreddit.new(limit=1):
            # post.upvote()
            print(f'REGGIE FRANZEN HAS LIKED "{post.title}"')
            time.sleep(30)
        print('...')
def getSubreddits():
    list = []
    for this_subreddit in reddit_rf.user.subreddits(limit=None):
        list.append(this_subreddit)
    return list 






def ReggieFranzen():
    subreddits = getSubreddits()
    likeXSubredditPosts(subreddits, 5)
    time.sleep(300)
    ## ENGAGE WITH ELIF
    respondToELIFPost()
    # time.sleep(300)
    ## ENGAGE WITH ANOTHER SUB
    # time.sleep(300)
    ## AND SO ON???



ReggieFranzen()




# def main():
#     while True:
#         ReggieFranzen()