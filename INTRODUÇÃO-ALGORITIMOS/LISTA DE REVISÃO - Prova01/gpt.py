
idade = int(input("Digite sua idade: "))
gestante = input("É gestante? (sim/não): ").lower()
estado_grave = input("Está em estado grave? (sim/não): ").lower()
dor = input("Nível de dor (leve/moderada/forte): ").lower()

if estado_grave == "sim":
    print("Grupo de atendimento: 1 (estado grave)")
elif idade >= 60:
    print("Grupo de atendimento: 2 (idoso)")
elif gestante == "sim":
    print("Grupo de atendimento: 3 (gestante)")
elif dor == "moderada":
    print("Grupo de atendimento: 4 (dor moderada)")
else:
    print("Grupo de atendimento: 5 (sem gravidade)")