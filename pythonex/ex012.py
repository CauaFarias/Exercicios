f = str(input('Digite uma Frase: ')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(f.count('A')))
print('Ela aprece pela primeira vez na posição {}'.format(f.find('A') + 1))
print('Ela aparece pela ultima vez na posição {}'.format(f.rfind('A') + 1))
