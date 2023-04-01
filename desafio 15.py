dias= float(input('Quantos Dias você utilizou o serviço de aluguel?'))
km= float(input('Quantos km foram rodados?'))

#km 0,15 / dia 60

totaldias=dias*60.00
totalkm= km*0.15
pagar= totaldias+totalkm

pago = (dias * 60) + (km*0.15)

print('O valor à pagar é de: R$ {:.2f}.'.format(pago))
