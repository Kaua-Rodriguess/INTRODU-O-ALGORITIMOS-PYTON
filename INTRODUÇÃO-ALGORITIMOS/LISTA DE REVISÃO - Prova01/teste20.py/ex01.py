numpar = 0
numimpar = 0
soma = 0
quantidade = 0

num = int(input("Digite um número: "))

while num < 10:
    if num % 2 == 0:
        numpar += 1
    else:
        numimpar += 1

    soma += num
    quantidade += 1

    num = int(input("Digite um número: "))

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print(numpar)
print(f"A média dos números é {media}")