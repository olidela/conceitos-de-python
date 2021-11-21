num = int(input('Digite um número: '))
tot = 0
for c in range(1, num):
    if num % c == 0:
        print(c)
        soma = tot + 1
print()
