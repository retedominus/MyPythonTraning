# Функция формирования многочленов с коэффициентом (от 0 до 10).
import random


def poly(k):
    strng = ""
    for i in range(k, 0, -1):
        coe = random.randrange(0, 10)
        op = random.choice(['+', '-'])
        if not coe == 0:
            strng += f'{coe}*x^{i}{op}'
    strng += f'{coe} = 0'
    return strng