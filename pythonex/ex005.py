from math import hypot
co = float(input('Comprimento do cateto opsto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))