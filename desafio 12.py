# ler o valor do produto e aplicar 5% de desconto

valor= float(input('Qual o Valor do Produto? R$\n'))

perc= valor - (valor*5/100)

print('O Produto no valor R${:.2f}, com 5% de desconto fica: R$ {:.2f}'.format(valor, perc))