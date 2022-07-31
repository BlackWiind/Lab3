from array import array
from math import sin, cos

c = 5
h = 0.023
x = c-h
derivatives = array('d', [])


def calc(var: float) -> float:
    return round(1 / c * sin(c * var), 4)


print("\t\tТаблица значений функции:\t\t")
print("\t******************************\t")
while x < c+16*h:

    print("\tx = %.4f" % x, "\t|\tf(x) = %.4f" % calc(x))
    derivatives.append((calc(x+h) - calc(x-h))/(2*h))
    x += h

print("\t******************************\t\n")
x = c-h
print("\t\t\tПриближенные и точные значения функции:\t\t")
print("\t*********************************************************\t")
print("\t\t x\t\t|\tприближенное\t|\tточное\t")
print("\t*********************************************************\t")
for i in range(derivatives.__len__()):
    print("\tx = %.4f" % x, "\t|\tf'(x) = %.4f" % derivatives[i], "\t|\tf'(x) = %.4f" % cos(x*c))
    x += h
print("\t*********************************************************\t")
