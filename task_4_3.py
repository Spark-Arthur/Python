import requests
from bs4 import BeautifulSoup
import datetime

def currency_rates(user_char):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(r.text, 'lxml')
    tags_char = soup.find_all(['charcode'])
    tags_val = soup.find_all(['value'])
    inx = 0
    for tag in tags_char:
        if tag.text == user_char:
            val_rub, val_kop = tags_val[inx].text.split(',')
            tags_val = f'{val_rub}.{val_kop}'
            tags_val = float(tags_val)
            d, m, y = soup.valcurs['date'].split('.')
            date = datetime.date(int(y), int(m), int(d))
            print(f'{round(tags_val, 2)}, {date}')
            q = '+'
            break
        else:
            inx += 1
            q = '-'
    if q == '-':
        print(None)

