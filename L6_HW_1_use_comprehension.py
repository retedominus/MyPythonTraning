# 1. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
from random import randrange


def list_creation(num=input("Enter the length of the list: ")):
    if num.isdigit() and int(num) > 0:
        return [randrange(1, 30) for i in range(int(num))]
    else:
        print("Error, the entered value cannot be used. Please, try again.")
        return 0


def bigger_val_ls(ls):
    return [ls[i] for i in range(1, len(ls)) if ls[i] > ls[i - 1]]


x_lst = list_creation()
print(x_lst)
print(bigger_val_ls(x_lst))


