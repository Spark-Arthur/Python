from random import choice

def get_jokes(num, flag='y'):
    '''
    "This func randomly get words from lists"
    :param num:
    :param flag:
    :return:
    '''
    joke_1 = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if flag == 'y':
        for i in range(num):
            joke = []
            joke.append(choice(nouns))
            joke.append(choice(adverbs))
            joke.append(choice(adjectives))
            joke =' '.join(joke)
            joke_1.append(joke)
    elif flag == 'n':
        for i in range(num):
            nou_j = choice(nouns)
            adv_j = choice(adverbs)
            adj_j = choice(adjectives)
            joke = []
            joke.append(nou_j)
            nouns.remove(nou_j)
            joke.append(adv_j)
            adverbs.remove(adv_j)
            joke.append(adj_j)
            adjectives.remove(adj_j)
            joke =' '.join(joke)
            joke_1.append(joke)
    return joke_1

print(get_jokes(5, 'n'))
print(get_jokes(5, 'y'))