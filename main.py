from __future__ import print_function, unicode_literals
from telethon import TelegramClient
from PyInquirer import prompt, print_json
import random
<<<<<<< HEAD
api_id = int(input("Input api_id\n"))
api_hash = input("Input api_hash\n")
channel_name = input("Input channel link\n")
users_list = []
with TelegramClient('anon', api_id, api_hash) as client:
    user_name = client.loop.run_until_complete(client.get_me()).username
    users = client.loop.run_until_complete(client.get_participants(channel_name))
    for i in range(len(users)):
=======

def workWithApi():
    api_id = int(input("Input api_id\n"))
    api_hash = input("Input api_hash\n")
    channel_name = input("Input channel link")
    users_list = []
    with TelegramClient('anon', api_id, api_hash) as client:
        user_name = client.loop.run_until_complete(client.get_me()).username
        users = client.loop.run_until_complete(client.get_participants(channel_name))
        for i in range(len(users)):
>>>>>>> 0bbdeca (pyinquirer init)
            users_list.append(users[i].username)
        users_list.remove(user_name)
        random.shuffle(users_list)
        winner = users_list[0]
        client.loop.run_until_complete(
            client.send_message(channel_name, f"И ПОБЕДИТЕЛЬ РОЗЫГРЫША - @{winner}. НАПИШИ МНЕ ПЫЖЫ, КСТА, ПОЗДРАВЛЯЮ С ПОБЕДОЙ")) #Change the text, but don't forget about var winner

def runForSingleWinner():
    question = [{
        'type': 'input',
        'name': 'prize',
        'message': 'What are you drawing?'
    }
    ]
    answer = prompt(question)

def main():
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
        runForSingleWinner()
    else:
        print("world")

if __name__ == "__main__":
    main()