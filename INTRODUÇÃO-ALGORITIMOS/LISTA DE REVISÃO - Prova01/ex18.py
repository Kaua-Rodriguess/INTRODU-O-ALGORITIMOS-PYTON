# GRUPO DE ATENDIMENTO PRIORITARIO
print("GRUPO DE ATENDIMENTO PRIORITARIO\n")
idade = int(input("Qual sua idade? "))
gestante = input("Você é gestante?(sim/não)")
pcd = input("Apresenta alguma deficiência?(sim/não)")

#CLASSE
print("\nCLASSE")
classe = input("Qual sua classe?(executiva/economica)")
categoria = input("Qual sua categoria?(ouro/prata/comun)")

#ATRASO
print("\nATRASO")
atraso = input("Chegou atrasado?(sim/não)")

if atraso == "sim":
    print("\nGRUPO: ATRASADOS (embarque por último)")

elif idade >= 60 or gestante == "sim" or pcd == "sim":
    print("GRUPO DE ATENDIMENTO PRIORITARIO\n")

elif classe == "executiva":
    print("GRUPO DA CLASSE EXECUTIVA\n")

elif categoria == "ouro":
    print("GRUPO: ECONOMICA - OURO\n")

elif categoria == "prata":
    print("GRUPO: ECONOMICA - PRATA\n")

else:
    print("GRUPO: ECONOMICA - COMUN\n")  


