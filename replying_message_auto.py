import requests
import key
import time

TOKEN = key.TOKEN
base_url = f'https://api.telegram.org/bot{TOKEN}'

chat_ids = ['-1002198877314', '-1002152186194']


def read_msg(offset):
    parameters = {
        'offset': offset,
        # 'chat_id': chat_ids[0],
    }
    resp = requests.get(base_url + '/getUpdates', data=parameters)
    data = resp.json()

    print(data)

    for result in data['result']:
        try:
            if "Assalomu alaykum" in result['message']['text']:
                # print(result['message']['chat']['id'])
                # send_msg(result['message']['chat']['id'])

                send_msg('-1002152186194')

        except KeyError:
            if 'Assalomu alaykum' in result['edited_message']['text']:
                # print(result['message']['chat']['id'])
                # send_msg(result['edited_message']['chat']['id'])

                send_msg('-1002152186194')
    if data['result']:
        return data['result'][-1]['update_id'] + 1


def send_msg(chat_id):
    parameters = {
        'chat_id': chat_id,
        'text': "Va alaykum assalom"
    }
    resp = requests.get(base_url + '/sendMessage', data=parameters)
    print(resp.text)


offset = 0

while True:
    offset = read_msg(offset)
