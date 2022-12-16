"""
Leia o salario de um trabalhador e o valor da prestação de um emprestimo. 
Se a prestação for maior que 20% do salario imprima: Emprestimo não concedido, caso contrario imprima: emprestimo concedido
"""

#Variaveis para ler o salario e o valor da prestação.
sal = float(input("Digite seu salario: "))
pres = float(input('Digite a prestação do emprestimo: '))

#Variavel para calcular o 20% do valor do salario.
nsal = sal * 0.20

#Condicionais para validar ou não o emprestimo.
if pres > nsal:
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido.')
