import requests
import key
import time

TOKEN = key.TOKEN
base_url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

chat_ids = ['-1002198877314', '-1002152186194']

image = 'https://tsdi.uz/assets/images/slider/stom.jpg'

parameters = {
    'photo': image,
    'caption': "Stomatologiya Instituti Morf binosi"
}

for chat_id in chat_ids:
    parameters['chat_id'] = chat_id
    response = requests.get(base_url, params=parameters)
    print(response.text)
