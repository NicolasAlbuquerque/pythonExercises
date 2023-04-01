#identificar se tem silva no nome

nomez=str(input('Digite seu nome: ').lower().strip())
nome=str(input('Digite seu nome completo:')).strip()
print('Silva Aparece no nome? {}'.format('silva' in nomez))
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

