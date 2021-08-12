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


print(thesaurus("Иван Сергеев", "инна серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
a = thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print('-----------')
# for i in sorted(a.keys()):
#     print(i, ':', a[i])
qw = {'И': ["Иван Сергеев"]}

print(qw['И'])