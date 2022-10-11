# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

def shuffle_list(list):
    import random
    out = []
    temp = []
    r_num = 0
    while len(out) != len(list):
        r_num = random.randrange(len(list))
        if r_num in range(len(list)) and not (r_num in temp):
            temp.append(r_num)
            out.append(list[r_num])
    return out

def create_list(x):
    ent = []
    for i in range(n):
        ent.append(i)
    return ent

n = int(input(("Enter length of the list: ")))
print(create_list(n))
print(shuffle_list(create_list(n)))
