p = float(input('Digite seu peso(kg): '))
a = float(input('Digite a sua altura(m): '))
imc = p / (a ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO IDEAL')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')