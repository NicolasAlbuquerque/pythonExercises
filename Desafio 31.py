#perunte a distancia em km
#calcule o preço da passagem
#se > 200 = 0,45
#else< 200= 0,50

print('-'*42)
print('---------------Rodoviária-----------------')
print('Aqui você paga por Km rodado!!!')
print('-'*42)
cidade=str(input('Qual a cidade de destino: ')).strip().upper()

km=float(input('Quantos km de distância: '))
if km > 200:
    print('O valor da sua Passagem para o destino {} é R${:.2f}'.format(cidade.capitalize(),km*0.45))
else:
    print('O valor da sua passagem para o destino {} é R$ {:.2f}'.format(cidade.capitalize(),km*0.50))