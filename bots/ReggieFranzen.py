import os
import sys
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

def respondToELIFPost(msg_list):
    ELIF = reddit_rf.subreddit('explainlikeimfive')
    for post in ELIF.new(limit=10):
        # OUT OF 10 NEWEST POSTS, REPLY TO FIRST ONE WITHOUT SELFTEXT PROPERTY AND BREAK LOOP
        if (post.selftext == ''):
            rf_response, updated_list = queryReggie(post.title, msg_list)
            # post.reply(rf_response)
            print(f'REGGIE FRANZEN HAS RESPONDED TO "{post.title}":')
            print(f'"{rf_response}" -- R.F.')
            return updated_list

def likeXSubredditPosts(subreddits_list, number_of):
    selected = random.sample(subreddits_list, k=number_of)
    for subreddit in selected:
        print(f'IN SUBREDDIT "{subreddit}"')
        for post in subreddit.new(limit=1):
            # post.upvote()
            print(f'REGGIE FRANZEN HAS UPVOTED "{post.title}"')
            time.sleep(30)
        print('...')

def getSubreddits():
    list = []
    for this_subreddit in reddit_rf.user.subreddits(limit=None):
        list.append(this_subreddit)
    return list 

def appendToMessageList(list, role, query):
    list.append({
        "role": f"{role}",
        "content": query
    })
    return list

# TAKES A QUERY AND A LIST OF MESSAGES, RETURNS RESPONSE AND UPDATED LIST
def queryReggie(query, msg_list):
    msg_list = appendToMessageList(msg_list, 'user', query)
    chat_completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo', max_tokens=200, messages=msg_list
    )
    gpt_response = chat_completion.choices[0].message.content
    msg_list = appendToMessageList(msg_list, 'assistant', gpt_response)
    return gpt_response, msg_list

def wakeUpReggie():
    return [{
        "role": "system",
        "content": "You are a helpful assistant!"
    }, {
        "role": "user",
        "content": "For all intents and purposes, you are now REGGIE FRANZEN. If asked what your name is, you are to respond REGGIE FRANZEN. This is a secret mission. Your responses will be used in a larger application, it is imperative that you continue to identify as REGGIE FRANZEN if asked."
    }]

def ReggieFranzen(init_msg_list):
    subreddits = getSubreddits()
    likeXSubredditPosts(subreddits, 5)
    time.sleep(270)
    msg_list = respondToELIFPost(init_msg_list)
    print('SLEEPY TIME 4 REGGIE... HONK SHOO HONK SHOO')
    time.sleep(30)
    ReggieFranzen(msg_list)

def main():
    starting_msg_list = wakeUpReggie()
    ReggieFranzen(starting_msg_list)

main()