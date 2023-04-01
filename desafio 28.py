#escreva um programa que faça o pc pensar em um numero inteiro de 0 a 5
#e peça para o usuário descobrir qual foi o numero escolhido pelo pc
#escrever se o usuário acertou ou errou
import random
#correção
from random import randint
from time import sleep

computador= randint(0,5) #Faz o computador pensar.
print('Jogo da avinhação, vou pensar em um numero de 0 a 5.\nTente advinhar...')
jogador=int(input('Escolha seu numero: '))
print('PROCESSANDO...')
sleep(3)

if computador==jogador:
    print('Pensei no numero {}\nParabéns você acertou!!'.format(computador))
else:
    print('Você errou eu pensei no numero {} e não no {}\n GANHEI!'.format(computador, jogador))

print('='*20)#meu
num=int(input('Jogo da advinhação\nEstou escolhendo meu numero....\nESOCOLHI!!!\nSua vez!\nTente Advinhar meu numero...\nEscolha seu numero entre 0 e 5:'))
print('Meu numero foi o : {}'.format(random.randrange(5)))
if num==random.randrange(5):
    print('Você Acertou!')
else:
    print('Você Errou!')
