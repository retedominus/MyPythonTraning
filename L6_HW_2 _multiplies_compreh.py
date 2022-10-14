# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.


def multiplicity(n=input("Enter the number greater then 20: ")):
    if n.isdigit() and int(n) > 20:
        return [i for i in range(20, int(n) + 1) if not i % 20 or not i % 21]
    else:
        print("Error, the entered value cannot be used. Please, try again.")
        return 0


print(multiplicity())
