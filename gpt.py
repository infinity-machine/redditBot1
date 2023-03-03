import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant!"
    }
]

while True:
    message = input('USER: ')
    if message:
        messages.append({
                "role": "user",
                "content": message
            })
        chat_completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo', messages=messages
        )
    reply = chat_completion.choices[0].message.content
    print(f"GPT: {reply}")
    messages.append({
        'role': 'assistant',
        'content': reply
    })
