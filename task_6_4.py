
nev = {}
with open('user_hobby.txt', encoding='utf-8') as f:
    for i in f:
        key, val = i.strip().split(':')
        nev[key] = val
print(nev)