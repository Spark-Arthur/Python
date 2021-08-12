def num_translate_adv(num):
    if num in num_dict:
        return num_dict[num]
    elif num.lower() in num_dict:
        return num_dict[num.lower()].title()
    else:
        return num_dict.get(num)

num_dict = {
        'one': '"один"',
        'two': '"два"',
        'three': '"три"',
        'four': '"четыре"',
        'five': '"пять"',
        'six': '"шесть"',
        'seven': '"семь"',
        'eight': '"восемь"',
        'nine': '"девять"',
        'ten': '"десять"'
    }
print(num_translate_adv("Fi;e"))