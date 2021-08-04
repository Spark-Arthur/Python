# Первое задание
duration = 400153
d_num = 86400
h_num = 3600
m_num = 60

d = duration // d_num # Считает дни

h1 = duration - (d_num * d)
h = h1 // h_num # Считает часы

m1 = h1 - (h_num * h)
m = m1 // m_num # Считает минуты

s = m1 - (m_num * m) # Считает секунды

if m == 0:
    print(f'{s} сек')
elif h == 0:
    print(f'{m} мин {s} сек')
elif d == 0:
    print(f'{h} час {m} мин {s} сек')
elif d != 0:
    print(f'{d} дн {h} час {m} мин {s} сек')







