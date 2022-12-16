"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utlizando as seguintes fórmulas (onde h corresponde a altura):
** Homens: (72.7 * h) - 58
** Mulheres: (62.1 * h) - 44.7
"""

h = float(input('Insira sua altura: '))
sexo = str(input('sexo [F/M]: ')).strip().upper()[0]
imc = 0

if sexo in 'F':
    imc = (62.1 * h) - 44.7
    print(f'Seu peso ideal é {imc}')
elif sexo in 'M':
    imc = (72.7 * h) - 58
    print(f'Seu peso ideal é {imc}')
else:
    print("Digite 'M' para Masculino e 'F' para Feminino")
