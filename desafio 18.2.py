from math import  sin
from math import cos
from math import  tan
from math import radians

ângulo= float(input('Digite um ângulo: '))

seno= sin(radians(ângulo))
cosseno= cos(radians(ângulo))
tangente= tan(radians(ângulo))

print('Com o ângulod e {:.2f}º, temos o seno no valor de {}'.format(ângulo,seno))
print('Com o ângulo de {:.2f}º, temos o cosseno no valor de {}'.format(ângulo,cosseno))
print('Com o ângulo de {:.2f}º, temos a tangente no valor de {}'.format(ângulo,tangente))
