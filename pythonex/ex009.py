name = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(name.upper()))
print('Seu nome em minusculas é {}'.format(name.lower()))
print('Seu nome tem {} letras'.format(len(name)-name.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(name.find(' ')))
separa = name.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

