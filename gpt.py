import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def gptResponse(input):
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=input,
        max_tokens=200,
        temperature=1
    )
    output = completion.choices[0].text.strip('\n\n')
    return output
