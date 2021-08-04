# a.
for i in range(1, 101):
    if i == 1 or i == 21 or i == 31 or i == 41 or i == 51 or i == 61 or i == 71 or i == 81 or i == 91:
        print(f'{i} процент')
    elif i == 2 or i == 3 or i == 4 or i == 22 or i == 23 or i == 24 or i == 32 or i == 33 or i == 34 or i == 42 or i == 43 or i == 44 or i == 52 or i == 53 or i == 54 or i == 62 or i == 63 or i == 64 or i == 72 or i == 73 or i == 74 or i == 82 or i == 83 or i == 84 or i == 92 or i == 93 or i == 94:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')
        
# b.
a = [1, 21, 31, 41, 51, 61, 71, 81, 91]
b = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94]
for i in range(1, 101):
    if i in a:
        print(f'{i} процент')
    elif i in b:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')