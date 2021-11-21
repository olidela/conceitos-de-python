import math

print('Insira um valor: ')
a = int(input())

print('Insira outro valor: ')
b = int(input())

print('Agora outro valor: ')
c = int(input())

if a < b and a < c :
    print(a, 'é o menor número')

elif b < a and b < c:
    print(b, 'é o menor número')

elif c < a and c < b:
    print(c, 'é o menor número')