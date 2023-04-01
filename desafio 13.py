# salário com 15% de aumento

salario = float(input('Qual o seu Salário Atual? '))

reajuste = salario + (salario * 15 / 100)

print('Seu salário com reajuste de 15% é de R${:.2f}'.format(reajuste))
