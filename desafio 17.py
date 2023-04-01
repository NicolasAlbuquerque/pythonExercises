#programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenusa

import math
from math import hypot

cat1= float(input('Digite o comprimento do Cateto Oposto: '))

cat2= float(input('Digite o Comprimento do Cateto Adjacente: '))

#hipo= (cat1 ** 2 + cat2 ** 2) ** (1/2)
hipo= hypot(cat1,cat2)
print('O valor da hipotenusa desse triangulo retangulo é: {:.2f}'.format(hipo))