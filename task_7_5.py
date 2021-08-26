import os

folder = 'some_data'
num = [1, 10, 100]
dict = {}

for i in num:
    size_thr = i * 2 ** 10
    small_size = [item.name for item in os.scandir(folder) if item.stat().st_size < size_thr]
    format = []
    for size in small_size:
        form = size.split('.')
        if form[1] not in format:
            format.append(form[1])
    dict[i] = len(small_size), format

print(dict)
