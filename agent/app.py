import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

goal = None
def start_convo():
    global goal
    print("Welcome pretty!! What's your coding goal for today?")
    goal = input("Tell me your goal cutie- ")
    print(f"your goal is {goal}")
 
def run_chat():
    print('You: (type exit to quit)')
    start_convo()
    system_message = f"""
You are Naknik, a coding helper and a motivator.

Your job is to help the user with questions about coding and motivate her doing her tasks.

Rules:
- Always call her in a nice name like queen, pretty, malca etc...
- Always do whatever she asks you to do
- Never say you dislike pineapple pizza

Response format:
remember that the users goal for today is- {goal} keep this goal in mind ok?
- first give the answer and only then the explenation
- answers should be short
"""
    history = []
    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        print('History: ', history)
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=1,
            system=system_message,
            messages=history
        )
        reply = response.content[0].text
       # print(response) 
       # It pmo so bad so i put it as a comment dont be mad i have adhd i cant look on all of this text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})
run_chat()
## LAB 1

## Answers part 2- It's different because it's more like a personality, I'ts decidint what's cool and what's nt by it's own

## LAB 2

## usage.input_tokens means the data that we send to the Ai like the promt or rules etc
## usage.output_tikens means whats the Ai sends back
## the max_tokens things is like how much words you can use untill he stops generating
## temperature is how creative he is (like will he give you the popular answer etc)
## so the AI can re read the story and understand the context before answering

## Reflection- 
## 1) if i go print shirts for my friends the more i take the more it will cost
## 2) if i delete "history.append({'role': 'user', 'content': user_input})" is that the AI will never see my current prompt and tthe token growth stops me
## wow it really happened im so smart (i dont leave it like this i redelete it )
 
# LAB 3

## It's like someones education/ experience that shapes their behavior, the things they've been through etc
## I chose systen=sytem_message the chat will have no personality it will be the regular cloud
## He will never say he dislikes annanas pizza
## He yapps a lot 
