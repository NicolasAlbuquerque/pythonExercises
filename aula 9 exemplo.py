#       manipulando string
#  manipulação de caracteres

#   fatiamento


frase = 'Curso em Video Python'
frase[9]
print(frase[9:13])  # mostra da 9 ao 13
# fatiamento, o ultimo não entra na contagem
print(frase[9:21:2])  # do 9 ao 20 pulando de 2 em 2
print(frase[:5])  # do 0 até o 4
print(frase[15:])  # do 15 até o final
print(frase[9::3])  # a partir de 9 pulando de 3 em 3

#       Análise

print(len(frase))  # Len= comprimento/ mostra o comprimento da frase
print(frase.count('o'))  # conta quantos 'o' minusculas
print(frase.count('o', 0, 13))  # fatia, e conta do espaço 0 ao 12
print(frase.find('deo'))  # mostra onde começa o deo
print(frase.find('Android'))  # quando não existe ele mostra o vallor -1 ou seja não exite
print('Curso' in frase)  # se curso está na string 'frase'

#        transformação
import re

print(frase.replace('Python', 'Android'))
print(frase.upper())  #maiuscula
print(frase.lower()) #minuscula
print(frase.capitalize())#deixa só a primeira letra minuscula
print(frase.title())#deixa todas as palavras com a primeira letra maicula
print(frase.strip())#exclui os espaços inuteis na string
frase.rstrip()# remove os espaços só do lado direiro
frase.lstrip()# remove os espaços só do lado esquerdo

            #divisão
print(frase.split())#divisão em uma lista considerando os espaços

        #Junção
print('-'.join(frase))
