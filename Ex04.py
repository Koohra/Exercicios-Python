print('-' * 40)
print('Bem vindo a calculadora simples digital')
print('Selecione a opção que deseja')
print('-' * 40)

print('(1) somar')
print('(2) Subtração')
print('(3) Divisão')
print('(4) Multiplicação')

menu = int(input(':'))

if menu > 0 and menu <= 4:
    n1 = float(input('Digite o numero: '))
    n2 = float(input('Digite outro numero: '))

    if menu == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} é igual {soma}')
    elif menu == 2:
        sub = n1 - n2
        print(f'{n1} - {n2} é igual {sub}')
    elif menu == 3:
        div = n1 / n2
        print(f'{n1} / {n2} é igual {div}')
    elif menu == 4:
        mult = n1 * n2
        print(f'{n1} x {n2} é igual {mult}')
else:
    print('Valor inserido invalido')

print('-' * 40)
print('Obrigado. Volte sempre!')
print('-' * 40)
