# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
from random import sample


def create_list(length):
    ls = sample(range(length * 2), length)
    return ls


def summa(x):
    res = 0
    index = 0
    for i in range(0, len(x) - 1, 2):
        res += x[i]
    return res


ls_output = create_list(int(input("Enter the length of the list: ")))
print(ls_output)
print(summa(ls_output))