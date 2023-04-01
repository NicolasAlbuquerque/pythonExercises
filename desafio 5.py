#faça um programa que leia um numero inteiro e mostre na tela seu sucessor e antecessor

num= int (input('Digite um valor:' ))
n1= (num - 1)
n2= (num + 1)
print('Você digitou o valor {}, o numero que o antecede é o numero {}, seu sucessor respectivamente é o nuemro {}'.format(num, n1, n2))

print('numero {} antecessor {} sucessor {}'.format(num, (num-1), (num+1)))