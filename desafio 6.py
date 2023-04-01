# programa que calcula o dobro o triplo e a raiz quadrada


n1 = int(input('Digite um valor: '))

d= n1*2
t=n1*3
r= n1**(1/2)#raiz quadrada


print ('você digitou: {}\n o dobro desse valor é {}\n o triplo do valor é {}\n e sua raiz quadrada é {}'.format(n1, d, t, r))
print ('vc digitou {} \n o dobro {}\n o triplo {}\n a raiz quadrada {}'.format(n1, (n1*2), (n1*3), pow(n1,(1/2))))