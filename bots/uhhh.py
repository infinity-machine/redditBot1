import os
import praw
import openai
import pprint
import random

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


def ReggieFranzen():
    for subreddit in reddit_rf.user.subreddits(limit=None):

        # for post in subreddit.new(limit=1):
        #     print(post.title)


ReggieFranzen()