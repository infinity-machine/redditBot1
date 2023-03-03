import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def respondToComment(comment):
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=comment,
        max_tokens=100,
        temperature=0
    )
    response = completion.choices[0].text.strip('\n\n')
    return response
