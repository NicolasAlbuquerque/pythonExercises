# programa que leia de  0 a 9999
# mostre os digitos separado por unidade dezenss centena e milhar


num = int(input('Digite um numero de 0 a 9999 com 4 digitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))

# print('UNIDADE', num[3:])
# print('DEZENA: ', num[2])
# print('CENTENA: ', num[1])
# print('MILHAR: ', num[0])
