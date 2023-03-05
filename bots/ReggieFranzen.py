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

# subreddit_ELIF = reddit_rf.subreddit('explainlikeimfive')


# def upvoteRecentSubredditPost(a_subreddit):
#     subreddit = reddit_rf.subreddit(a_subreddit)
#     for post in subreddit.new(limit=1):
#         # post.upvote()
#         print(f"REGGIE FRANZEN HAS UPVOTED POST '{post.title}'IN SUBREDDIT '{subreddit}'")











# def chooseRandomSelections(subreddit_list):
#     # GET ONE TO THREE USER SUBREDDITS
#     for x in range(random.randint(1, 3)):
#         this_subreddit = subreddit_list[random.randint(0, (len(subreddit_list) - 1))]
#         print(this_subreddit)
#         # upvoteRecentSubredditPost(this_subreddit)


# def getSubreddits(reddit_instance):
#     list = []
#     for this_subreddit in reddit_instance.user.subreddits(limit=None):
#         list.append(this_subreddit)
#     return sorted(list)

# def upvoteSomePosts():
#     subreddits = getSubreddits(reddit_rf)
#     print(subreddits)
#     # selections = chooseRandomSelections(subreddits)

def ReggieFranzen():
    # LIST OF SUBREDDITS ON USER
    # upvoteSomePosts()
    for subreddit in reddit_rf.user.subreddits():
        print(subreddit)
    # print(reddit_rf.user.subreddits())



ReggieFranzen()














## BETTER WAY TO DO THIS?
## OUT OF THE 10 NEWEST REDDIT POSTS, PICK THE FIRST THAT DOES NOT HAVE A BODY PROPERTY AND RETURN
# def grabELIFPost():
#     for post in subreddit_ELIF.new(limit=10):
#         if post.selftext == '':
#             return post


# openai.api_key = os.getenv('OPENAI_API_KEY')

# def gptResponse(input):
#     completion = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=input,
#         max_tokens=200,
#         temperature=1
#     )
#     output = completion.choices[0].text.strip('\n\n')
#     return output

# pprint.pprint(dir(reddit_rf))