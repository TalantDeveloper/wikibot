import requests
import key
import time

TOKEN = key.TOKEN
base_url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'

chat_ids = ['-1002198877314', '-1002152186194']

audio = 'https://tsdi.uz/storage/elon/6986937251071513.mp3'

parameters = {
    'audio': audio,
    'caption': "Yaxshilik qolar insondan"
}

for chat_id in chat_ids:
    parameters['chat_id'] = chat_id
    r = requests.get(base_url, params=parameters)
    print(r.text)
