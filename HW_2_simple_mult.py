# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def smpl_mult(num):
    ls = []
    x = num
    for i in range(x - 1, 0, -1):
        if not num % i:
            temp = num // i
            ls.append(temp)
            num = num // temp
    return ls


print(smpl_mult(int(input("Enter the number: "))))

