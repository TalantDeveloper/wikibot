import requests

# import key

TOKEN = "7652126290:AAGX-UjXsVVAs_Ah0sHgjm3_BzhL9iaRB5A"

# rest = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
# print(rest.text)

# offset
# rest = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=313233808")
# print(rest.text)


# rest = requests.get('https://api.telegram.org/bot' + TOKEN + '/' + 'getUpdates')
# for update in rest.json()['result']:
#     print(update['update_id'], update['message']['message_id'], 'text: ', update['message']['text'])


base_url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

parameters = {
    'offset': '1834494100',
    'limit': '100',
}

while True:
    rest = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
    print(rest.text)
# first = response.json()
# print(first)

# second = first['result']
# length = len(second)
# print(second[length - 1])
# print(second[length - 1]['channel_post']['message_id'])
# print(second.last())


# datas = {'update_id': 313234014, 'channel_post': {'message_id': 41,
#                                                   'sender_chat': {'id': -1002481531999, 'title': 'Majburiy obuna',
#                                                                   'username': 'majburiyobunaqilish', 'type': 'channel'},
#                                                   'chat': {'id': -1002481531999, 'title': 'Majburiy obuna',
#                                                            'username': 'majburiyobunaqilish', 'type': 'channel'},
#                                                   'date': 1737615840, 'text': 'fsdfa'}}
