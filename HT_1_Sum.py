# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num = input("Введите вещественное число: ")
summ = 0
n = len(num) - 2
num = float(num) * 10 ** n
count = len(str(num)) - 2
for i in range(count):
    summ += num % 10
    num //= 10
print(round(summ))
