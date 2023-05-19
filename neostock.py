import requests
import json
import re
from bs4 import BeautifulSoup

if __name__ == '__main__':

    # source
    url = 'https://neostocks.info/'
    response = requests.get(url=url)
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # get json data
    script_tags = soup.find_all('script', string=re.compile("^window.__data__"))
    for tag in script_tags:
        string = str((tag.string)[18:])

    json_s = json.loads(string)

    for json in json_s['summary_data']['1d']:
        print('{} \nopen:{} curr:{} change:{}'.format(json['ticker'], json['open'], json['curr'], json['change']))