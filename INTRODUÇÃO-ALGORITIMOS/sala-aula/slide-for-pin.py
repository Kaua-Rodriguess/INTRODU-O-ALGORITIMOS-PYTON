pin = ""

for contador in range(1,5):
    digito = input(f"Digite o dígito{contador}")
    
    while int(digito) < 0 or int(digito) > 9:
     digito = input(f"Digito inválido. Digite um valor entre 0 e 9: ")

     pin += digito

print(f"PIN digitado: {pin}")