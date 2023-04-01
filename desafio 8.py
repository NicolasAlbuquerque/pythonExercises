#escreva um programa que leia o valor em metros, e mostre ao usuárioo o valor centimetros e milimetros.
mq= int(input('Digite um valor em Metros : '))
mm= mq*1000
cm= mq*100
print('{} metros quadrados são equivalentes a {} centimetos e {} milimetros.'.format(mq, cm, mm))