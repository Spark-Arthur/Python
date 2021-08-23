from itertools import zip_longest
import sys
user_hob = {}
list_h = []
list_u = []
with open('users.csv', encoding='utf-8') as u, open('hobby.csv', encoding='utf-8') as h:
    for line_u in u:
        for line_h in h:
            list_h.append(line_h.strip())
        list_u.append(line_u.strip())
    if len(list_u) < len(list_h):
        sys.exit(1)
    else:
        user_hob = dict(zip_longest(list_u, list_h))
        with open('user_hobby.txt', 'w', encoding='utf-8') as i:
            for key, val in user_hob.items():
                i.write(f'{key}:{val}\n')

