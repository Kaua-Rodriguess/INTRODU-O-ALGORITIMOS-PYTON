pontuacoes = []

for i in range(3):
    jogador = []
    print(f"\n JOGADOR {i+1}")
    
    for j in range(5):
        pontos = int(input(f"Partida {j+1}: "))
        jogador.append(pontos)

    pontuacoes.append(jogador)