# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def names_dict(*st):
    dictionary = {}
    for name in st:
        char = name[0]  # первая буква имени
        if char not in dictionary:  # проверяем содержит ли словарь такой ключ
            dictionary[char] = [name]  # в словаре первой букве имени (ключ) присваиваем значение - имя
        else:
            dictionary[char] += [name]  # если в словаре уже есть такая первая буква, присваиваем ей
    return dictionary


print(names_dict("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))


#
# from itertools import groupby
#
#
# def thesaurus(*args):
#     if "" not in args:
#         return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
#     return "Error"
#
#
# print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))