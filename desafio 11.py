alt= float(input('Qual a altura da parede ?'))
larg= float (input("Qual a Largura da Parede? "))

mq= alt*larg

print('A sua parede tem a dimensão de {} x {} e sua área tem {} m²'.format(larg, alt ,mq ))
tinta= mq/2
print('Para pintar essa parede de {}m², você precisará de {}l de tinta.'.format(mq,  tinta))