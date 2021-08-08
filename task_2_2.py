list_1 = ['в', '5', 'часов', '-107', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']

num_list = []
for i in list_1:
    if i[0] in '+' or i[0] in '-':
        a = list_1.index(i)
        num_list.append(i)
        list_1[a] = 'isdunfi'
        list_1.insert(a, '"')
        a += 2
        list_1.insert(a, '"')

    elif i.isdigit():
        a = list_1.index(i)
        num_list.append(i)
        list_1[a] = 'isdunfi'
        list_1.insert(a, '"')
        a += 2
        list_1.insert(a, '"')

num = ''
for i in num_list:
    if i[0] == '+':
        num += f'{i[0]}{int(i):02d}.'
    elif i[0] == '-':
        num += f"{i[0]}{int(i.replace('-', '', 1)):02d}."
    else:
        num += f'{int(i):02d}.'

num1 = num.split('.')

inx = 0
for i in list_1:
    if i == 'isdunfi':
        a = list_1.index(i)
        list_1[a] = num1[inx]
        inx += 1

my_str = ' '.join(list_1)
print(my_str)






