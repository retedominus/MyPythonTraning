# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
from random import randrange


def ls_create(opera, num):
    if num < 0:
        print("Error. Negative value of the number of numbers!")
    return opera(num)


def uniq_num_ls(lst):
    u_lst = []
    my_dict = {}.fromkeys(lst, 0)  # примечание: из списка lst формируется словарь уникальных значений
    # где в качестве ключа - элемент списка, значение = 0

    for i in lst:
        my_dict[i] += 1  # запись в словарь значений (+1) по количеству ключей в списке lst
    for j in my_dict:
        if my_dict[j] == 1:
            u_lst.append(j)

    return u_lst


ls = ls_create(lambda num: [randrange(1, num) for i in range(num)], int(input("Enter the real number: ")))


print(ls)
print(uniq_num_ls(ls))
