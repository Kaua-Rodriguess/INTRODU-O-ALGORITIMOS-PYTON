notas = [7.5,8.0,6.5,9.0,8.5]

maior_nota = notas[0]

#nota assume o primeiro valor da lista para comparar 
# com o primeiro e assim sucessivamente
for nota in notas:
    if nota > maior_nota:
        maior_nota = nota

print(f"A maior nota dentro dessa lita é: {maior_nota}")        