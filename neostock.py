import sys
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

    tickers = []
    path = 'ticker.txt'
    with open(path) as f:
        for line in f.readlines():
            s = line.split('\n')
            tickers.append(s[0])

    soup = BeautifulSoup(response.text, 'html.parser')

    # get json data
    script_tags = soup.find_all('script', string=re.compile("^window.__data__"))
    for tag in script_tags:
        string = str((tag.string)[18:])

    json_s = json.loads(string)

    type = int(sys.argv[1])

    def case(i):
        switcher={
                0 : json_s['summary_data']['1d'],  ## Read ticker from txt
                1 : json_s['hot_stocks'],          ## Hot
                2 : json_s['summary_data']['1d'],  ## Stocks price [ 15 ~ 20 ]
                3 : json_s['summary_data']['1d']   ## All stocks
        }
        return switcher.get(i,"Invalid type of case")

    # message
    message = "%-7s%-7s%-7s%-7s" % ('Ticker' , 'Open' , 'Curr' , 'Change') + '\n'

    for json in case(type):
        if type == 0:
            for ticker in tickers:
                if json['ticker'] == ticker:
                    message += "%-7s%-7s%-7s%-7s" % (json['ticker'] , format(json['open']) , format(json['curr']) , format(json['change'])) + '\n'
        if type == 1:
            for hot_json in case(0):
                if json['ticker'] == hot_json['ticker']:
                    message += "%-7s%-7s%-7s%-7s" % (hot_json['ticker'] , format(hot_json['open']) , format(hot_json['curr']) , format(hot_json['change'])) + '\n'
        if type == 2:
            if json['curr'] >= 15 and json['curr'] < 20:
                message += "%-7s%-7s%-7s%-7s" % (json['ticker'] , format(json['open']) , format(json['curr']) , format(json['change'])) + '\n'
        if type == 3:
            message += "%-7s%-7s%-7s%-7s" % (json['ticker'] , format(json['open']) , format(json['curr']) , format(json['change'])) + '\n'

    print(message)

    # send
    message = '```\n' + message + '```\n'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message

    response = requests.get(send_text)