from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Света', 'Артур'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '10В'
]

new_list = list(zip_longest(tutors, klasses, fillvalue=None))
for i in range(len(tutors)):
    print(new_list[i])
