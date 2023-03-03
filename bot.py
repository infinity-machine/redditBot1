import os
import praw
# import random
# import pprint

from dotenv import load_dotenv
load_dotenv()

# from gpt import respondToComment
# from utils import getProperties

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
)

subreddit = reddit.subreddit('explainlikeimfive')


# GRAB A "RANDOM" POST FROM ELIF
# "RAMDOM" = ONE RANDOMLY SELECTED *RECENT* POST THAT *DOES NOT* HAVE SELFTEXT PROPERTY

# GENERATE GPT RESPONSE TO POST AND REPLY WITH GENERATED RESPONSE



# for post in subreddit.new(limit=1):
#     print("---post---\n")
#     print("Title: ", post.title)
#     print("Text: ", post.selftext)
#     print("Score: ", post.score)
#     print("---post---\n")
    
#     for comment in post.comments:
#         if hasattr(comment, 'body'):
#             print("---comment---\n")
#             print(comment.body)
#             print("---comment---\n")

# for post in subreddit.new(limit=5):
#     print(post.title)

# print(getProperties(subreddit.new()))




