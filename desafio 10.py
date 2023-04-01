#crie um programa que converta reais em dolaresd

print('-'*50)
din= float(input('Quantos Reais você tem? R$'))
doll= din/5.13
euro= din/5.35
rublo=din/11.45
libra= din/6.16
print('Com R$ {:.2f} Reais, você pode comprar US$ {:.2f} Dolares.'.format(din, doll))
print('Com R$ {:.2f} Reais, você pode comprar € {:.2f} Euros'.format(din, euro))
print('Com R$ {:.2f} Reais, você pode comprar ₽ {:.2f} Rublos'.format(din, rublo))
print('Com R$ {:.2f} Reais, você pode comprer £ {:.2f} Libras Esterlinas'.format(din, libra))


print('-'*50)