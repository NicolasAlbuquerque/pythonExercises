#texo qualquer
#quantidade de A
#primeira e ultima vez que aparece no texto
frase=str(input('Digite uma frase: ')).strip()
frase= frase.upper()
print('Quantas vezes a Letra A aparece na frase: {}'.format(frase.count('A')))
print('primeira posição que ocorre a letra A: {} '.format(frase.find('A')+1))
print('A ultima posição que a letra A ocorre é {}'.format(frase.rfind('A')+1))



