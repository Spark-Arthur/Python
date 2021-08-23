import pprint

result = []

with open('file_pars.txt', encoding='utf-8') as f:
    for line in f:
        str_list = line.split()
        ip = str_list[0]
        result.append((ip, str_list[5].lstrip('"'), str_list[6]))
pprint.pprint(result)
