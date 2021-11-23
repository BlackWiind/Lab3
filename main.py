from array import array
from math import sin, cos

c = 5
h = 0.023
x = c-h
derivative = array('d', [])


def calc(_x):
    return round(1/c * sin(c*_x), 4)


print("\tТаблица 1:\t")
while x < c+16*h:

    print("\tx = %.4f" % x, "\t|\tf(x) = %.4f" % calc(x))
    derivative.append(calc(x+h) - calc(x-h)/(2*h))
    x += h

x = c-h
print("\tТаблица 2:\t")
for i in derivative:
    print("\tx = ", x, "\t|\tf'(x) = %.4f" % derivative[i], "\t|\tf'(x) = %.4f" % cos(x*c))
    x += h
    