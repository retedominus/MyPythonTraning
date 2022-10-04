#  5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Негофибоначчи!
def neg_fib(num):
    x, y = 1, 1
    ls = [0]
    for i in range(num):
        ls.append(x)
        ls.insert(0, x * (-1) ** i)
        x, y = y, x + y

    return ls


print(*neg_fib(int(input("Enter the number: "))))
