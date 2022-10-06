# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
from random import randrange
from collections import Counter


def ls_create(opera, num):
    if num < 0:
        print("Error. Negative value of the number of numbers!")
    return opera(num)


def uniq_num_ls(lst):
    u_lst = []
    c = Counter(lst)
    for i in lst:
        if c[i] == 1:
            u_lst.append(i)
    return u_lst


ls = ls_create(lambda num: [randrange(1, num) for i in range(num)], int(input("Enter the real number: ")))


print(ls)
print(uniq_num_ls(ls))







# Counter(map(lambda x: x[1],  big_data_list))