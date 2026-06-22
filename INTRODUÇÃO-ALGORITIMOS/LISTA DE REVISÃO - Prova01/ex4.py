n = int(input("Digite um valor inteiro: "))

cedulas = [100, 50, 20, 10, 5, 1]

for cedula in cedulas:
    qtd = n // cedula
    print(f"Necessário {qtd} cédulas de {cedula}")

    n = n % cedula