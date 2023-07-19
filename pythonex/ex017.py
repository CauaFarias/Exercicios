vc = float(input('Qual o valor da casa que voçê vai comprar: R$'))
sa = float(input('Qual o seu salário mensal: '))
qa = int(input('Em quantos anos você vai pagar a casa: '))
pr = vc / (qa * 12)
mi = sa * 30 / 100
print('Para pagar uma casa de R${:.2f} en {} anos, a prestação é de R${:.2f}'.format(vc, qa, pr))
if pr <= mi:
    print('\033[32mEmprestimo CONCEDIDO!')
else:
    print('O valor da prestação excedeu 30% do seu salario!')
    print('\033[31mEmprestimo NEGADO!')
