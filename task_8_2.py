import re

RE_NAME = re.compile(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$)')
RE_NAME_ip = re.compile(r'([0-9a-z]{0,4})?:([0-9a-z]{0,4})?:([0-9a-z]{0,4})?:([0-9a-z]{0,4})?:([0-9a-z]{0,4})?:([0-9a-z]{0,4})?(:[0-9a-z]{0,4})?(:[0-9a-z]{0,4})?$')

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        str_list = line.split()
        ip = str_list[0]
        if RE_NAME.match(ip) != None:
            datetime = str_list[3].strip('[]'), str_list[4].strip('[]')
            datetime_mix = ' '.join(datetime)
            print((ip, datetime_mix, str_list[5].strip('"'), str_list[6], str_list[8], str_list[9]))
        else:
            if RE_NAME_ip.match(ip) != None:
                datetime = str_list[3].strip('[]'), str_list[4].strip('[]')
                datetime_mix = ' '.join(datetime)
                print('@' * 100)
                print((ip, datetime_mix, str_list[5].strip('"'), str_list[6], str_list[8], str_list[9]))
                print('@' * 100)
            else:
                raise ValueError(f'wrong ip: {ip}')
