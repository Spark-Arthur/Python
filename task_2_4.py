my_list = ['инженер-конструктор саня', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(my_list)):
    new_list = my_list[i].split(" ")
    ind = len(new_list) -1
    list_name = new_list[ind]
    name = list_name.lower().title()
    my_list.append(name)

for i in range(1):
    my_list.remove(my_list[i])
for i in range(2):
    my_list.remove(my_list[i])
for i in range(1):
    my_list.remove(my_list[i])

print(f'Привет {my_list[0]}!')
print(f'Привет {my_list[1]}!')
print(f'Привет {my_list[2]}!')
print(f'Привет {my_list[3]}!')
