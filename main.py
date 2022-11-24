from telethon import TelegramClient
import random
api_id = int(input("Input api_id\n"))
api_hash = input("Input api_hash\n")
channel_name = input("Input channel link\n")
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
