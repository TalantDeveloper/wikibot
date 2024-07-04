import requests

TOKEN = '1881218661:AAFcllZI3Kf4ivPKlpmUFtC6Zfo88_GbBGc'


# rest = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
# print(rest.text)


# offset
# rest = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=313233808")
# print(rest.text)


# rest = requests.get('https://api.telegram.org/bot' + TOKEN + '/' + 'getUpdates')
# for update in rest.json()['result']:
#     print(update['update_id'], update['message']['message_id'], 'text: ', update['message']['text'])
