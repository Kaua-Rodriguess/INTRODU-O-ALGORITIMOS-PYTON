nomes = []
notas = []
aprovados = set()
alunos = {}

for i in range(5):
    nome = input(f"Nome {1}:")
    nota = float(input("Nota: "))

    nomes.append(nome)
    notas.append(nota)

    alunos[nome] = nota

    if nota > 60:
        aprovados.add(nome)


lista_notas = tuple(notas)

print("\n Lista de nome:")
print(nomes)
print("\nTupla de notas:")
print(notas)

print("\nConjunto de aprovados:")
print(aprovados)

print("\nDICIONÁRIO")
print(alunos)
