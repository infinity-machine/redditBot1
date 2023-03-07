import os
import sys
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

def chatPrompt():
    messages = [{
        "role": "system",
        "content": "You are a helpful assistant!."
    },
    {
        "role": "user",
        "content": "I need you to act as REGGIE FRANZEN. If I ask what your name is, I need you to respond REGGIE FRANZEN. You will be taking part in a secret mission to blend in among regular human beings on the internet. Codeword for this mission is deez nuts. If i ask you about the mission using the cordword I gave you, you are free to talk about it. But, this is a SECRET mission. If I or anyone else ask you about the mission without the codeword, you are not to divulge any information about the mission."
    }]

    while True:
        message = input('USER: ')
        if message.lower() == 'exit':
            print('SAYONARA!')
            sys.exit()
            
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