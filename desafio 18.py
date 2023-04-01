# leia um angulo qualquer
# exiba seno cosceno e coseno e tangente
import math

ang = float(input('Digite um angulo: '))

seno = math.sin(math.radians(ang))
cos= math.cos(math.radians(ang))
tang= math.tan(math.radians(ang))



print('o Angulo {} tem o seno {:.2f}'.format(ang,seno))
print('O angulo {} tem o cosseno de {:.2f}'.format(ang,cos))
print('O angulo{}, tem a Tangente de {:.2f}'.format(ang, tang))


print('='*60)
print("Com um angulo de {}º, obtemos:  ".format(math.ceil(ang)))
print('Seno {:.2f}'.format(math.sin(ang)))
print('Cosseno {:.2f}'.format(math.cos(ang)))
print('Tangente {:.5f}'.format(math.tan(ang)))


