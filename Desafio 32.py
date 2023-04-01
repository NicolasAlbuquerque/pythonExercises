#programa que leia o ano
#dizer se é ou não ano bissexto


ano=int(input('Digite um ano: '))
if (ano%4==0 and ano %100 !=0 or ano % 400 ==0) :
    print('o ano de {} é um ano Bissexto!'.format(ano))
else:
    print('O ano de {} não é um ano Bissexto!'.format(ano))