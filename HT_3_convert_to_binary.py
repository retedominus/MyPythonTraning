# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.


def dec_to_bin(num):
    ls = []
    while num > 0:
        ls.append(num % 2)
        num = num // 2
    ls.reverse()
    return ls


def print_list(lst):
    for i in range(len(lst)):
        print(lst[i], end="")


print_list(dec_to_bin(int(input("Enter the number: "))))

