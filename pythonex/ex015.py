from time import sleep
print('='*70)
print('Ooh não, você acabou de passar em um radar e não prestou atenção')
print('='*70)
v = int(input('Qual a sua velocidade quando ultrapassou o radar? '))
print('Buscando multa...')
sleep(3)
if v < 81:
    print('Você não foi multado, estava dentro do limite de velocidade')
else:
    print('Você ultrapassou o limite permitido de 80km/h')
    multa = (v - 80) * 7
    print('Você recebeu uma multa de {}R$'.format(multa))
