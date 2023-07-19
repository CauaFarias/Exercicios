from random import randint
print('Tente adivinhar qual o numero que o computador está pensado de 0 a 5')
ia = randint(0, 5)
n = int(input('O computador ja pensou, agora tente descobrir: '))
if n == ia:
    print('Parabens, você acertou')
else:
    print('Você perdeu, o computador pensou no numero {} e vc no {}'.format(ia, n))

