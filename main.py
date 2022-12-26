from __future__ import print_function, unicode_literals
from telethon import TelegramClient
from PyInquirer import prompt, print_json
import random


api_id = 0
api_hash = ""
channel_name = ""

def work_with_api():
    api_id = int(input("Input api_id\n"))
    api_hash = input("Input api_hash\n")
    channel_name = input("Input channel link")
    users_list = []
    with TelegramClient('anon', api_id, api_hash) as client:
        user_name = client.loop.run_until_complete(client.get_me()).username
        users = client.loop.run_until_complete(client.get_participants(channel_name))
        for i in range(len(users)):
            users_list.append(users[i].username)
        users_list.remove(user_name)
        random.shuffle(users_list)
        winner = users_list[0]
        client.loop.run_until_complete(
            client.send_message(channel_name, f"И ПОБЕДИТЕЛЬ РОЗЫГРЫША - @{winner}. НАПИШИ МНЕ ПЫЖЫ, КСТА, ПОЗДРАВЛЯЮ С ПОБЕДОЙ")) #Change the text, but don't forget about var winner

def run_for_single_winner():
    question = [{
        'type': 'input',
        'name': 'prize',
        'message': 'Enter your prize'
    }
    ]
    answer = prompt(question)

def main():
    global api_id
    global api_hash
    global channel_name
    question = [
        {
            'type':'input',
            'name': 'api_id',
            'message': 'Enter your api_id'
        },
        {
            'type': 'input',
            'name': 'api_hash',
            'message': 'Enter your api_hash'
        },
        {
            'type': 'input',
            'name': 'channel_name',
            'message': 'Enter link to your channel'
        }
    ]
    answer = prompt(question)
    api_id = int(answer['api_id'])
    api_hash = answer['api_hash']
    channel_name = answer['channel_name'] 
    ask_winners_amount()

def ask_winners_amount():
    question = [
        {
            'type': 'list',
            'name': 'theme',
            'message': 'Amount of winners',
            'choices': [
                'One',
                'Multiple',
            ]
        },
    ]
    answers = prompt(question)

    if answers['theme'] == "One":
        run_for_single_winner()
    else:
        print("world")

if __name__ == "__main__":
    main()