linhas_invalidas = 0

arquivo = open("./leitura.txt","r")

for linha in arquivo: #percorro cada linha do arquivo

    linha = linha.strip() #remove o "\n" do final da linha
    partes = linha.split(";") #quebra a linha em pedaços, criando assim um vetor

    if len(partes) != 3: #se a linha não possuir exatamente 3 campos

        linhas_invalidas +=1

    else:
        codigo = partes[0]
        data = partes[1]
        temperatura_texto = partes[2]

        try:
            temperatura = float(temperatura_texto) #verifica se a temperatura pode virar um numero real

            print("Linha válida")
            print("Sensor",codigo)
            print("Data:",data)
            print("Temperatura:",temperatura)

        except ValueError:
            linhas_invalidas += 1


arquivo.close()