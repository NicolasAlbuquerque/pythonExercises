#desenvolva um programa que leia o comprimento de 3 retas e diga se pode ou náo se um triangulo

# A soma das medidas de dois lados dos triangulos severá SEMPRE ser maior > que o terceiro lado!


r1=int(input('Entre com o tamanho da primeira Reta: '))
r2=int(input('Entre com o tamanho da segunda Reta: '))
r3=int(input('Entre com o tamanho da terceira Reta: '))
if (r1+r2>r3 and r3+r2 > r1 and r3+r1 > r2):
    print('As retas estão dentro dos padrões de existencia,e formam um Triangulo!')
else:
    print('As retas não estão dentro dos padrões de existenci de um triangulo.')