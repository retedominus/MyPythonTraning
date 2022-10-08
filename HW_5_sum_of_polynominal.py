# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
import random
import Library as lb


# with open('poly_2.txt', 'a') as data:
#     for i in range(random.randrange(2, 4)):
#         data.write(f'{lb.poly(int(input("Enter the natural degree: ")))}\n')
#     data.write(lb.poly(int(input("Enter the natural degree: "))))

# f = open('poly.txt', 'r')
# data_1 = f.read() + ''
# f.close()
# f_2 = open('poly_2.txt', 'r')
# data_2 = f_2.read() + ''
#
# while data_1 != '':
#     end_body_pos = data_1.index('=')
#     arg = data_1[:end_body_pos]

with open('poly.txt', 'r') as file_1:
    poly_1 = file_1.readline()
with open('poly_2.txt', 'r') as file_2:
    poly_2 = file_2.readline()



# if len(poly_1) == len(poly_2):
#     poly_1.append(poly_2)
# else:
#     print("Error")
print(poly_1.replace(' = 0', poly_2))


from random import choice


# def poly_sum(name_1: str, name_2: str):
#     with open(name_1, "r", encoding="utf-8") as my_f_1, \
#             open(name_2, "r", encoding="utf-8") as my_f_2:
#         first = my_f_1.readlines()
#         second = my_f_2.readlines()
#
#         if len(first) == len(second):
#             with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
#                 for i, v in enumerate(first):
#                     my_f_3.write(f"{v[:-5]} + {second[i]}")
#         else:
#             print("The contents of the files do not match!")
#
#
# # poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
# poly_sum("poly.txt", "poly_2.txt")