result = list()
num_req = dict()

with open('file_pars.txt', encoding='utf-8') as f:
    for line in f:
        str_list = line.split()
        ip = str_list[0]
        result.append((ip, str_list[5].lstrip('"'), str_list[6]))
        num_req[ip] = num_req.get(ip, 0) + 1

    spam = ['ip', 0]
    for ip, num in num_req.items():
        if num > spam[1]:
            spam[0] = ip
            spam[1] = num

    print('IP:', spam[0])
    print('Колличество запросов:', spam[1])






