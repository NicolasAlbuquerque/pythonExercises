#sorteiro de alunos entre 1 e 4
#ler os nomes e mostras o sorteeado

import _random
import random

print('='*20)

aluno1= str(input('Digite o nome do Aluno: '))
aluno2= str (input('Digite o nome do aluno: '))
aluno3=str (input('Digite o nome do Aluno: '))
aluno4=str(input('Digite o nome do aluno: '))


list= [aluno1, aluno2, aluno3,aluno4]
print('O Aluno sorteado para apagar a lousa foi o: {}'.format(random.choice(list)))
