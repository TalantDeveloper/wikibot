import requests
import key
import time

TOKEN = key.TOKEN
base_url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

chat_ids = ['-1002198877314', '-1002152186194']

file = 'https://tsdi.uz/storage/elon/topshiriq-xati-44-bayon.pdf'
file_1 = 'https://tsdi.uz/assets/images/slider/stom.jpg'

parameters = {
    'document': file_1,
    'caption': "Buyruq"
}

for chat_id in chat_ids:
    parameters['chat_id'] = chat_id
    response = requests.get(base_url, params=parameters)
    print(response.text)

