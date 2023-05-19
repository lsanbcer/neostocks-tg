import requests
import json
import re
from bs4 import BeautifulSoup

if __name__ == '__main__':

    # tg bot
    bot_token = 'your tg bot token'
    bot_chatID = 'your tg chat id'

    # source
    url = 'https://neostocks.info/'
    response = requests.get(url=url)
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # get json data
    script_tags = soup.find_all('script', string=re.compile("^window.__data__"))
    for tag in script_tags:
        string = str((tag.string)[18:])

    json_s = json.loads(string)

    print('Ticker   Open     Curr     Change')

    # message
    message = str('Ticker   Open     Curr     Change\n')

    for json in json_s['summary_data']['1d']:
        print('{:5}'.format(json['ticker']) + '{:5}'.format(json['open']) + '{:5}'.format(json['curr']) + '{:5}'.format(json['change']))
        message += "%-9s%-9s%-9s%-9s" % (json['ticker'] , format(json['open']) , format(json['curr']) , format(json['change'])) + '\n'

    # send
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)