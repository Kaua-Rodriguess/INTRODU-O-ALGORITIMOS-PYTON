def eliminar_duplicatas(lista):
    nova_lista = []

    for numero in lista: #A cada repetição "NÚMERO" possui o valor de cada elemento da lista
      existe = False

      for elemento in nova_lista: #A cada repetição "ELEMENTO" possui o valor de cada elemento da nova lista
        if elemento == numero:
           existe = True

      if existe == False:
        nova_lista.append(numero)

    return nova_lista

#PROGRAMA PRINCIPAL

lista = []

print("Digite:")

for i in range(20):
   n = int(input(f"{i+1}º numero: "))
   lista.append(n)

resultado = eliminar_duplicatas(lista)

print(f"Lista original:{lista}")
print(f"Lista sem repetição:{resultado}")