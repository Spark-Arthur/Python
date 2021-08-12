def thesaurus(*names):
    list_name = [*names]
    dict = {}
    for name in list_name:
        name = name.title()
        key = name[0]
        if key in dict:
            dict[key].append(name)
        else:
            new_dict = {key: [name]}
        dict.update(new_dict)
    return dict

a = thesaurus("Майа", "Дарси", 'Макс', "рома", "дима", 'артур')
print(a)
for i in sorted(a.keys()):
    print (i, ':', a[i])