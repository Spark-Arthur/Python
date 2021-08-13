import requests
from bs4 import BeautifulSoup as BS

def currency_rates(user_char):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    html = BS(r.content, 'html.parser')
    date_code = html.select('ValCurs')
    date_code = str(date_code)
    date = date_code[16:26]
    for i in range(34):
        currency_code = html.select('CharCode')[i]
        value_code = html.select('Value')[i]
        currency_code = str(currency_code)
        currency = currency_code[10:13]
        value_code = str(value_code)
        value_code = value_code[7:14]
        value_code_rub, value_code_kop = value_code.split(',')
        value_code = f'{value_code_rub}.{value_code_kop}'
        value_code = float(value_code)
        if user_char == currency:
            print(f'1 {currency}')
            print(type(currency))
            print(f'{value_code} RUB')
            print(type(value_code))
            print(date)
            print(type(date))
            q = '+'
            break
        else:
            q = '-'
    if q == '-':
        print(None)



currency_rates('HKD')