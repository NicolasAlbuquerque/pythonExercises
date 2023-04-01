#programa que identifica se a cidade começa com a palavra santo

cidade=str(input('Digite o nome da Sua cidade: ')).strip()

cidade=cidade.capitalize()

print('Tem a palavra Santo no nome da cidade? {}'.format('Santo'in cidade))