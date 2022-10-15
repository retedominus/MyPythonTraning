# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)


from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def jokes(n: int, unique: bool = False) -> list:

    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    j_lst = []
    lst_min = min(no, adv, adj)

    for i in range(len(lst_min) % n if unique else n):
        num = randrange(len(lst_min))
        j_lst.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}" if unique else
                     f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    return j_lst


print(jokes(10))


