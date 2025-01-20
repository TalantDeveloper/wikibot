import requests
import key

TOKEN = key.TOKEN

rest = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
print(rest.text)

# offset
# rest = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=313233808")
# print(rest.text)


# rest = requests.get('https://api.telegram.org/bot' + TOKEN + '/' + 'getUpdates')
# for update in rest.json()['result']:
#     print(update['update_id'], update['message']['message_id'], 'text: ', update['message']['text'])


base_url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

parameters = {
    'offset': '556841744',
    'limit': '100',
}
response = requests.get(base_url, data=parameters)
print(response.text)

