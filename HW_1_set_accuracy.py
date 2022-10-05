# Вычислить число c заданной точностью d
from decimal import Decimal


print(Decimal(str(input("Enter the real number: "))).quantize(Decimal(str(input("Enter the required accuracy '0.0001':")))))


