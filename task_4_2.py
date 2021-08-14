import requests
from bs4 import BeautifulSoup

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
            print(type(tags_val))
            print(tags_val)
            q = '+'
            break
        else:
            inx += 1
            q = '-'
    if q == '-':
        print(None)

currency_rates('USD')