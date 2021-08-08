my_list = [57.8, 46.51, 97, 93.3, 5.78, 3, 12.5, 2.1, 56, 2.8]
s = ''
for i in my_list:
    if i == int(i):
        i_rub = i
        i_kop = 0
    else:
        i_rub = int(i)
        num = str(i).split('.')
        i_kop = int(num[1])
    s += f'{i_rub} руб {i_kop:02d} коп, '

print(s)
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

for i in range(5):
    print(my_list[i])
