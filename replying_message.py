import requests
import key
import time

TOKEN = key.TOKEN
base_url = f'https://api.telegram.org/bot{TOKEN}'

chat_ids = ['-1002198877314', '-1002152186194']


def read_msg():
    parameters = {
        'offset': '313233817',
        # 'chat_id': chat_ids[0],
    }
    resp = requests.get(base_url + '/getUpdates', data=parameters)
    data = resp.json()
    for result in data['result']:
        try:
            if "Python" in result['message']['text']:
                # print(result['message']['chat']['id'])
                send_msg(result['message']['chat']['id'])
        except KeyError:
            if 'Python' in result['edited_message']['text']:
                # print(result['message']['chat']['id'])
                send_msg(result['edited_message']['chat']['id'])


def send_msg(chat_id):
    parameters = {
        'chat_id': chat_id,
        'text': "dfsdfsdfsdf"
    }
    resp = requests.get(base_url + '/sendMessage', data=parameters)
    print(resp.text)


read_msg()

