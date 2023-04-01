#programa que mostre o nome em todo em maiuscula
#o nome com todas minusculas
#Quantas letras sem contar espaços
#quantas letras tem o perimeiro nome



#nome=str(input('Qual seu nome completo: '))
#print(nome.upper())
#print('='*20)
#print(str.lower(nome))
#print('='*20)
#total=nome.replace(' ','')
#print('Seu nome no total {} letras'.format(len(total)))
#print('='*20)
#print(nome)
#primeiro=nome.split()
#print('O Seu primeiro nome tem {} letras.'.format(len(primeiro[0])))

print('_'*20)
print('_'*20)


nome= str(input('Digite seu nome Completo:')).strip()
print('seu nome em maiuscula é {}'.format(nome.upper()))
print('seu noem em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {}'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa= nome.split()
print('seu primeiro nome é {}, e ele tem {} letras'.format(separa[0],len(separa[0])))







