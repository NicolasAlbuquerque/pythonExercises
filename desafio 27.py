#programa que leia nome completo e mmostre semparadamente os dois

nome=str(input('Digite seu nome: ')).split()
#last=nome.pop()
print('Primeiro nome: ', nome[0])
#print('Sobrenome:', last)
print('Sobrenome {}'.format(nome.pop()))