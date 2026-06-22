total_salario = 0
total_filhos = 0
quantidade_pessoas = 0
maior_salario = 0
ate_mil = 0

salario = float(input("Digite o salário (negativo para encerrar): "))

while salario >= 0:
    filhos = int(input("Digite o número de filhos: "))

    total_salario += salario
    total_filhos += filhos
    quantidade_pessoas += 1

    if salario > maior_salario:
        maior_salario = salario

    if salario <= 1000:
        ate_mil += 1

    salario = float(input("Digite o salário (negativo para encerrar): "))

if quantidade_pessoas > 0:
    media_filhos = total_filhos / quantidade_pessoas
    media_salario = total_salario / quantidade_pessoas
    percentual_ate_mil = (ate_mil / quantidade_pessoas) * 100

    print(f"Média do número de filhos: {media_filhos:.2f}")
    print(f"Média do salário: R$ {media_salario:.2f}")
    print(f"Maior salário: R$ {maior_salario:.2f}")
    print(f"Percentual com salário até R$1000,00: {percentual_ate_mil:.2f}%")
else:
    print("Nenhum dado foi informado.")