print(f"Conversão para binário! \n")

n = int(input("Digite um numero binário: "))

resultado = 0
expoente = 0 

while n > 0:
 digito = n % 10 #pego o ultimo numero

 resultado += digito * (2**expoente)
 n //= 10 #tiro o ultimo numero, porque como é um inteiro, ele não lê a parte decimal

 expoente +=1

print (f"Resultado em decimal: {resultado}")