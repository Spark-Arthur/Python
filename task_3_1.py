def num_translate(num, num_dict):
    if num in num_dict:
        return num_dict[num]
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
print(num_translate("eight", num_dict))