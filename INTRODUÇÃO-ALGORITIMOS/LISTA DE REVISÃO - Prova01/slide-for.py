pin = 0

for i in range(4):
    digito = int(input("Digite um dígito: "))
    pin = pin * 10 + digito

print(f"PIN completo: {pin}")