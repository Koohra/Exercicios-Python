"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre
** O número digitado ao quadrado
** A raiz quadrada do número digitado
"""

from math import sqrt
n = float(input('Digite um número: '))

if n > 0:
    quad = n ** 2
    raiz = sqrt(n)
    print(f'O quadrado {n} é igual {quad} é a raiz quadrada é {raiz} ')
else:
    print('Número invalido.')