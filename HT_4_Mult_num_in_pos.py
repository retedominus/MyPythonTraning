#Напишите программу, которая принимает на вход 2 числа.
#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных позициях(не индексах).
n = int(input("Enter number of element: "))
pos_1 = int(input("Enter position one: "))
pos_2 = int(input("Enter position two: "))
list = []
for i in range(n * -1, n + 1):
    list.append(i)
print(list[pos_1 - 1] * list[pos_2 - 1])