# 4.* Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.
import random
import Library as lb


with open('poly.txt', 'w') as data:
    for i in range(random.randrange(2, 4)):
        data.write(f'{lb.poly(int(input("Enter the natural degree: ")))}\n')
    data.write(lb.poly(int(input("Enter the natural degree: "))))




