#crie um programa qque leia um numero real qualquer
#peloo teclado e mostre sua porção inteira
#ex digite um numero :6.127
#o numero 6.127 tem a parte inteira 6


import math
num= float (input('digite um numero Real: '))
#print('o numero real {}, tem a parte inteira: {}'.format(num,math.floor(num)))
print('O umero Real {}, tem como parte inteira o valor de: {} '.format(num, math.trunc(num)))
print('O valor do numero real {}, tem como sua porção inteira o valor de:{}'.format(num, int(num)))