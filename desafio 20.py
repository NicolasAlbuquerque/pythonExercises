#ordem de apresentação do trabalho





import _random
import random
print('='*70)
print('='*4,'Sorteiro da Apresentação dos trabalhos','='*5)
a1=str(input('\t Nome do Aluno: '))
a2=str(input('\t Nome do Aluno: '))
a3=str(input('\t Nome do Aluno: '))
a4=str(input('\t Nome do Aluno: '))

lista= [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem do sorteiro será...')
print(random.sample([a1,a2,a3,a4], k = 4))
print('A ordem de apresentação será: ')
print(lista)