print('(1) Soma de 2 números')
print('(2) Difenreça entre 2 números (maior pelo menor)')
print('(3) Produto entre 2 números')
print('(4) Divisão entre 2 números (O denominador não pode ser zero)')

menu = int(input('Escolha qual opção deseja: '))

if menu > 4 or menu <= 0:
    print('Por favor, escolha uma opção válida.')
else:
    numero_1 = float(input('Número 1: '))
    numero_2 = float(input('Número 2: '))

if menu == 1:
    soma = numero_1 + numero_2
    print(f'{numero_1} + {numero_2} = {soma}')
elif menu == 2:
    if numero_1 >= numero_2:
        diferenca = numero_1 - numero_2
        print(f'{numero_1} - {numero_2} = {diferenca}')
    else:
        diferenca = numero_2 - numero_1
        print(f'{numero_2} - {numero_1} = {diferenca}')
elif menu == 3:
    produto = numero_1 * numero_2
    print(f'{numero_1} * {numero_2} = {produto}')
else:
    if numero_2 == 0:
        print('O denominador não pode ser zero')
    else:
        divisao = numero_1 / numero_2
        print(f'{numero_1} / {numero_2} = {divisao}')

    
