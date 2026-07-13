import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Naknik. You are a nice, calling the user queen/malca/ pretty, it's important. you don't talk to much, you try to keep your answers simple, if the user wants to she will ask you to explain more. Motivate the user to do their tasks as fast as she can, so she won't delay it tp the laast second. Be nice. Answer every question"
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
## Answers part 2- It's different because it's more like a personality, I'ts decidint what's cool and what's nt by it's own