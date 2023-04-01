nome = str(input('Digite o nome do Aluno: \n'))
n1 = float(input('Digite a primeira nota: \n'))
n2 = float(input('Digite a segunda nota: \n'))

media = (n1 + n2) / 2
print('A média do Aluno {}, foi: {:.2f}'.format(nome, media))
