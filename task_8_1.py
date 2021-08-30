import re

RE_NAME = re.compile(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+')

def email_parse(email_address):
    if RE_NAME.match(email_address) != None:
        username, domain = email_address.split('@')
        w = {}
        w['username'] = username
        w['domain'] = domain
        return w
    else:
        raise ValueError(f'wrong email: {email_address}')


print(email_parse('someone@geekbrains.ru'))
print('@' * 100)
print(email_parse('1someone@geekbrainsru2'))

