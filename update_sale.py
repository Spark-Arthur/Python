import sys

def update_sale(num, value):
    with open('bakery.csv', encoding='utf-8') as f:
        old_data = []
        for val in f:
            old_data.append(val.strip())
        old_data[num - 1] = value
    with open('bakery.csv', 'w', encoding='utf-8') as f:
        for val in old_data:
            f.write(f'{val}\n')

num_s = len(sys.argv)
num = int(sys.argv[1])
value = sys.argv[2]
if num_s == 3 and num <= num_s:
    update_sale(num, value)
else:
    print('EROR')