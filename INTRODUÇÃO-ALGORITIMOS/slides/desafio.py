## for i in range(len(valores)): aqui ele vai até o tamanho do lista
# for x in valores: aqui o indice assume os valores da lista 

# ENTRADA:
#5 inteiros
#
#PROCESSO:
# armazenar
# 
#SAIDA:
# exibir na ordem inversa

lista []

for i in range(3):
    n = int(input("Digite um número: "))
    lista.append(n)

print("Ordem inversa")

for i in range(len(lista) - 1,-1,-1):
    print(lista[i])

