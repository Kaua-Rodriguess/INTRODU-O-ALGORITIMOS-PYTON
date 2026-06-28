sensores = {}
linhas_invalidas = 0

maior_temperatura_geral = None
sensor_maior_temperatura = ""

arquivo = open("leituras.txt", "r")

for linha in arquivo:
    linha = linha.strip()
    partes = linha.split(";")

    if len(partes) != 3:
        linhas_invalidas += 1
    else:
        codigo = partes[0]
        data = partes[1]
        temperatura_texto = partes[2]

        try:
            temperatura = float(temperatura_texto)

            if codigo not in sensores:
                sensores[codigo] = {
                    "quantidade": 0,
                    "soma": 0,
                    "menor": temperatura,
                    "maior": temperatura
                }

            sensores[codigo]["quantidade"] += 1
            sensores[codigo]["soma"] += temperatura

            if temperatura < sensores[codigo]["menor"]:
                sensores[codigo]["menor"] = temperatura

            if temperatura > sensores[codigo]["maior"]:
                sensores[codigo]["maior"] = temperatura

            if maior_temperatura_geral is None or temperatura > maior_temperatura_geral:
                maior_temperatura_geral = temperatura
                sensor_maior_temperatura = codigo

        except ValueError:
            linhas_invalidas += 1

arquivo.close()


saida = open("relatorio_sensores.txt", "w")

for codigo in sensores:
    quantidade = sensores[codigo]["quantidade"]
    menor = sensores[codigo]["menor"]
    maior = sensores[codigo]["maior"]
    media = sensores[codigo]["soma"] / quantidade

    linha_relatorio = (
        f"Sensor: {codigo} | "
        f"Quantidade: {quantidade} | "
        f"Menor: {menor:.2f} | "
        f"Maior: {maior:.2f} | "
        f"Média: {media:.2f}"
    )

    print(linha_relatorio)
    saida.write(linha_relatorio + "\n")

print(f"\nLinhas inválidas: {linhas_invalidas}")
print(f"Sensor com maior temperatura: {sensor_maior_temperatura} ({maior_temperatura_geral:.2f})")

saida.write(f"\nLinhas inválidas: {linhas_invalidas}\n")
saida.write(f"Sensor com maior temperatura: {sensor_maior_temperatura} ({maior_temperatura_geral:.2f})\n")

saida.close()