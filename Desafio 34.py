#pergunte o salario
#calcule o aumento
#if 1250,00 > 10%
#else 15%

print('Calculo de Aumento')
print('Salário acima de R$ 1.250,00 receberão aumento de 10%\nSalários abaixo deste valor serão reajustados em 15%.')
sal=float(input('Qual o valor da sua Remuneração Mensal?'))
if sal >= 1250.00:
    #sal1= sal+ (sal*15)/100
    print('Seu Salário Atual é de R$ {:.2f}\nCom o reajusto estipulado em 10%\nVocê passará a ter uma Remuneração Mensal de R${:.2f}'.format(sal,sal+(sal*10)/100))
else:print('Sua Remuneração atual é de R$ {:.2f}\nCom Reajuste estipuládo em 15%\nVocê passará a ter uma Remuneração mensal de R${:.2f}'.format(sal,sal+(sal*15)/100))
