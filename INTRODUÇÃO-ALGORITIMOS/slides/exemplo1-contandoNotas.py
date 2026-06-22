notas = [7.5,8.0,6.5,9.0,8.5]

contador = 0

for nota in notas:
    if nota > 6.0:
        contador += 1

print(f"Tem {contador} notas maiores que 6.0")