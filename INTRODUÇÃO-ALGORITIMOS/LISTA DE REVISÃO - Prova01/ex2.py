print(f"Cálculo de potência!\n")


b = int(input("Informe a base: "))
ex = int(input("Informe o expoente: "))


resultado = 1

for i in range(ex):
    resultado = resultado * b

print(f"{b} elevado á {ex} é igual a {resultado}")