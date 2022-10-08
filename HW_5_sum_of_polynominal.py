# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.

def poly_sum(arg_1: str, arg_2: str):
    with open(arg_1, "r", encoding="utf-8") as my_f_1, \
            open(arg_2, "r", encoding="utf-8") as my_f_2:
        first = my_f_1.readlines()  # записали содержимое файла 1 в виде массива
        second = my_f_2.readlines()

        if len(first) == len(second):  # сравнили длинны "массивов"
            with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3: # создан итоговый файл
                for i, v in enumerate(first):  # проходим по итерируемому объекту содержащему i - номер и v - его знач-е
                    my_f_3.write(f"{v[:-5]}+{second[i]}")  # i - номер строки v - строка [:-5] (минус 5 знаков)
        else:
            print("The contents of the files do not match!")


poly_sum("poly.txt", "poly_2.txt")
