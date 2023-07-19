n = input('Digite o numero que deseja ver a tabuada: ')
for c in range(1, 11):
    t = n * c
    print('{} x {:2} = {}'.format(n, c,n * c))