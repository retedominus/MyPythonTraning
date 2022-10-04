# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
from random import uniform


def real_num_list_creation(number):
    ls = []
    if number <= 0:
        print("Incorrect value is entered!")
        return [0.0]

    for i in range(number):
        ls.append(round(uniform(0, number), 2))
    return ls


def max_min_dif(lst):
    ls = []
    for i in range(len(lst)):
        ls.append(round(lst[i] % 1, 2))
    res = round(max(ls) - min(ls), 2)
    print(f"Max: {max(ls)}, Min: {min(ls)}, Difference: {res}")
    return res


output_lst = real_num_list_creation(int(input("Enter the number: ")))

print(output_lst)
print(max_min_dif(output_lst))
