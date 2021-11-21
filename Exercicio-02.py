import math

print('Insira um valor: ')
a = int(input())

print('Insira outro valor: ')
b = int(input())

print('Agora outro valor: ')
c = int(input())

if a > b + c or b > a + c or c > b + a:
    print(a, b, c, 'não são medidas de um triângulo')

elif a == b and a == c:
    area = a**2 * math.sqrt(3) / 4
    print(a, b, c, ' são medidas de um triângulo equilátero')
    print(area, ' é a área deste triângulo')

if a > b and a > c:
    if a**2 == b**2 + c**2:
        area = b*c / 2
        print(a, b, c, ' são medidas de um triângulo retângulo')
        print(area, ' é a área deste triângulo')

elif b > a and b > c:
    if b**2 == a**2 + c**2:
        area = a*c / 2
        print(a, b, c, ' são medidas de um triângulo retângulo')
        print(area, ' é a área deste triângulo')

elif c > a and c > b:
        if c ** 2 == a ** 2 + b ** 2:
            area = a * b / 2
            print(a, b, c, ' são medidas de um triângulo retângulo')
            print(area, ' é a área deste triângulo')

if a == b and a!=c:

    altura = math.sqrt(a**2 -(c/2)**2)
    area = (c * altura)/2

    print(a, b, c, ' são medidas de um triângulo isóceles')
    print(area, ' é a área deste triângulo')

if a == c and a!=b:
        altura = math.sqrt(a**2 - (b/2)**2)
        area = (b * altura) / 2

        print(a, b, c, ' são medidas de um triângulo isóceles')
        print(area, ' é a área deste triângulo')

if b == c and b!=a:

        altura = math.sqrt(b ** 2 - (a / 2) ** 2)
        area = (a * altura) / 2

        print(a, b, c, ' são medidas de um triângulo isóceles')
        print(area, ' é a área deste triângulo')