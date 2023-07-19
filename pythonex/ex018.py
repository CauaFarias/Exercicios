nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2) / 2
print('Sua media foi {:.1f}'.format(m))
if m < 5.0:
    print('\033[31mREPROVADO')
elif 7 > m > 5.0:
    print('\033[31mRECUPERAÇÃO')
else:
    print('\033[32mAPROVADO')
