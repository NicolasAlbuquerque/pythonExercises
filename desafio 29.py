#Programa que leia a velocidade do carro
#Se ultrapassar 80km mostrar uma mensagem dizendo que foi multado
#a multa vai custar R$7,00 por cada km acima do permiitdo

print('===========DEPARTAMENTO DE TRANSITO===========')
km=int(input('Qunatos km por hora você está: '))
if km> 80:
    print('Você Recebeu uma multa.\nNo valor de: R${:.2f}'.format((km-80)*7.00))
else:
    print('Você está dentro do limite de Velocidade!')