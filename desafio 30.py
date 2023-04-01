#Programa que leia um numero inteiro e diga se é par ou impar


num=int(input('Digite um numero: '))
if (num%2)==0:
    print('O número é Par!')
else:
    print('O número é Impar!')

print('impar'if (num%2) else 'par')

if num%2:
    print('impar')
else:
    print('par')