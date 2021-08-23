import sys

list_s = []

def add_sale(num):
    list_s.append(num)

add_sale(sys.argv[1])

with open('bakery.csv', 'a', encoding='utf-8') as f:
    for val in list_s:
        f.write(f'{val}\n')

