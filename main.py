from __future__ import print_function, unicode_literals
from telethon import TelegramClient
from PyInquirer import prompt, print_json
import random


api_id = 0
api_hash = ""
channel_name = ""
prize = []
prize_amount = 0

def work_with_api():
    global api_id 
    global api_hash
    global channel_name
    users_list = []
    print(type(api_hash), api_hash)
    print(type(api_id), api_id)
    with TelegramClient('anon', api_id, api_hash) as client:
        user_name = client.loop.run_until_complete(client.get_me()).username
        users = client.loop.run_until_complete(client.get_participants(channel_name))
        for i in range(len(users)):
            users_list.append(users[i].username)
        users_list.remove(user_name)
        random.shuffle(users_list)
        winners = users_list[0:prize_amount]
        for i in range(0, prize_amount):
            client.loop.run_until_complete(
                client.send_message(channel_name, f"{i+1} place. Winner @{winners[i]}. Prize: {prize[i]}")) #Change the text, but don't forget about var winner

def ask_for_prize():
    global prize
    question = [{
        'type': 'input',
        'name': 'prize',
        'message': 'Enter your prize'
    }
    ]
    answer = prompt(question)
    answer_str = answer['prize']
    prize = answer_str.split(" ")
    while len(prize) != prize_amount:
        print(f"You not entered {prize_amount} prizes. Try again")
        question = [{
            'type': 'input',
            'name': 'prize',
            'message': 'Enter your prize'
            }
        ]
        answer = prompt(question)
        answer_str = answer['prize']
        prize = answer_str.split(" ")
    work_with_api()
    

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
    api_hash = str(answer['api_hash'].split(" "))
    api_id = int(answer['api_id'])    
    channel_name = str(answer['channel_name'].split(" ")) 
    ask_winners_amount()

def ask_winners_amount():
    global prize_amount
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
        prize_amount = 1
    else:
        question = [
            {
                'type': 'input',
                'name': 'prize_amount',
                'message': 'Write amount of prizes',
            },
        ]
        answers = prompt(question)
        prize_amount = int(answers["prize_amount"])
    ask_for_prize()


if __name__ == "__main__":
    main()