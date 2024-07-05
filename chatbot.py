import requests
import key
import pandas as pd

TOKEN = key.TOKEN

url = 'https://raw.githubusercontent.com/vikasjha001/telegram/main/qna_chitchat_professional.tsv'
df = pd.read_csv(url, sep='\t')

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
        conf = {'chat_id': '-1002152186194', 'message': result['message']['text']}
        send_msg(conf)

    if data['result']:
        return data['result'][-1]['update_id'] + 1


def auto_answer(message: str):
    answer = df.loc[df['Question'].str.lower() == message.lower()]

    if not answer.empty:
        answer = answer.iloc[0]['Answer']
        return answer
    else:
        return "Sorry, I could not understand you !!!"


def send_msg(conf):

    answer = auto_answer(conf['message'])

    parameters = {
        'chat_id': conf['chat_id'],
        'text': answer
    }
    resp = requests.get(base_url + '/sendMessage', data=parameters)
    # print(resp.text)


offset = 0

while True:
    offset = read_msg(offset)
