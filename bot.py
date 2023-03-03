import os
import praw
# import random
import pprint

from dotenv import load_dotenv
load_dotenv()

from gpt import respondToComment
from utils import getProperties

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
)

subreddit = reddit.subreddit('explainlikeimfive')

# for post in subreddit.new(limit=1):
#     pprint.pprint(getProperties(post))


# for post in subreddit.new(limit=1):
#     print("---post---\n")
#     print("Title: ", post.title)
#     print("Text: ", post.selftext)
#     print("Score: ", post.score)
#     print("---post---\n")
#     post.reply(my_response)
    
#     for comment in post.comments:
#         if hasattr(comment, 'body'):
#             print("---comment---\n")
#             print(comment.body)
#             print("---comment---\n")

# for post in subreddit.new(limit=1):
#     print(post.title)
#     post.reply(respondToComment(post.title))






