arq1 = open("./nomes1.txt","r")
arq2 = open("./nomes2.txt","r")


l1 = []
l2 = []

nomes_mesclados = []


for linha in arq1:
    l1.append(linha.strip()) #strip() serve para não imprimir o "enter"

for linha in arq2:
    l2.append(linha.strip())

tam1 = len(l1)
tam2 = len(l2)

while(i < tam1 and j < tam2):
    if(l1[i] < l2[j]):
        nomes_mesclados.append(l1[i])
        i+=1
    else:
        nomes_mesclados.append(l2[j])
        j+=1

print(nomes_mesclados)

    
arq1.close()
arq2.close()

