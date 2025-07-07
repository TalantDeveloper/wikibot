import types

import requests
# from telegram import InlineKeyboardMarkup, InlineKeyboardButton

# import key
import time

# TOKEN = key.TOKEN
TOKEN = ""

base_url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# check_btn = InlineKeyboardMarkup(row_width=1)
# check_btn.add(
#     InlineKeyboardButton(text="1 - kanalimiz", url=channel_url),
#     InlineKeyboardButton(text="2 - kanalimiz", url=channel_url1),
#     InlineKeyboardButton(text="✅ Tekshirish", callback_data="checksub"),
# )

chat_ids = ['-1002481531999', '-1002152186194']

# parameters = {
#     'chat_id': chat_ids[0],
#     'text': 'Assalomu alaykum bugun 17.01.2025'
# }
#
# response = requests.get(base_url, data=parameters)
# print(response.text)

# Ko'p habar bir vaqtda yuborish
# texts = ['Assalomu alaykum',
#          'Bugun osmon ochiq boladi',
#          'harorat 35 gradus issiq bolishi kutilmoqda',
#          'kun davomida koproq suv iching'
#          ]
# for text in texts:
#     time.sleep(5)
#     parameters['text'] = text
#     parameters['chat_id'] = chat_ids[1]
#     response = requests.get(base_url, data=parameters)
#     print(response.text)

TOKEN = "5356590968:AAGBMDJ-y6RX-3Ts1H_YgVQH35HEdqHWv38"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": '7759697535',
    'text': "Assalomu alaykum! \nHurmatli foydalanuvchi (Yulduz). Sizning murojaatingiz yetib keldi."
}

response = requests.post(url, json=payload)
print(response.json())

