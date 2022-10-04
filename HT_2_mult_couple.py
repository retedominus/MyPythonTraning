# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import sample  # не стоит ли вызов прописывать в функции?


def create_ls(length: int):
    if length < 0:
        print("Incorrect value is entered!")
        return []

    ls = sample(range(length * 2), length)
    return ls


def mult_couple(lst):
    new_ls = []
    arg1 = (len(lst) // 2)
    tsl = list(reversed(lst))
    if len(lst) % 2 == 0:
        for i in range(0, arg1):
            new_ls.append(lst[i] * tsl[i])
    else:
        for i in range(0, arg1):
            new_ls.append(lst[i] * tsl[i])
        new_ls.append(lst[arg1])
    return new_ls


in_lst = create_ls(int(input("Enter the length of the list: ")))
print(in_lst)
print(mult_couple(in_lst))
