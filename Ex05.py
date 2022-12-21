a = float(input('Digite o valor do lado 1 do triangulo: '))
b = float(input('Digite o valor do lado 2 do triangulo: '))
c = float(input('Digite o valor do lado 3 do triangulo: '))

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    if a == b == c:
        print('Triangulo equilátero')
    elif ((a == b) and a != c)  or ((a == c) and a != b) or ((b ==c) and b != a):
        print('Trangulo isósceles')
    elif a != b != c:
        print('Triangulo escaleno')
else:
    print('Não é um triangulo')