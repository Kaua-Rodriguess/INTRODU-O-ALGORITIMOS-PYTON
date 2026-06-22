menor_preco = None
maior_preco = None
soma = 0

for i in range(7):
    preco = float(input(f"Digite o preço da {i+1}ª loja: "))

    if menor_preco is None or preco < menor_preco:
        menor_preco = preco

    if maior_preco is None or preco > maior_preco:
        maior_preco = preco

    soma += preco

media = soma / 7

print(f"Menor preço: R$ {menor_preco:.2f}")
print(f"Maior preço: R$ {maior_preco:.2f}")
print(f"Média dos preços: R$ {media:.2f}")