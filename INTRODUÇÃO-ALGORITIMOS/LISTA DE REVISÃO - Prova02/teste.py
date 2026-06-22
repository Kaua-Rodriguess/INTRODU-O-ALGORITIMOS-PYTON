# Sistema de biblioteca
# Chave = ISBN
# Valor = [titulo, autor, quantidade em estoque]

biblioteca = {
    "9788535914849": ["A República", "Platão", 10],
    "9788578270698": ["Ética a Nicômaco", "Aristóteles", 5]
}


def emprestar_livro(biblioteca, isbn):
    # Verifica se o ISBN existe
    if isbn not in biblioteca:
        print("ISBN não encontrado.")
        return

    # biblioteca[isbn][2] = quantidade em estoque
    if biblioteca[isbn][2] < 1:
        print("Não há livros em estoque.")
    else:
        biblioteca[isbn][2] -= 1
        print("Livro emprestado com sucesso!")

    print(f"Quantidade em estoque: {biblioteca[isbn][2]}")


def devolver_livro(biblioteca, isbn):
    # Verifica se o ISBN existe
    if isbn not in biblioteca:
        print("ISBN não encontrado.")
        return

    biblioteca[isbn][2] += 1
    print("Livro devolvido com sucesso!")
    print(f"Quantidade em estoque: {biblioteca[isbn][2]}")


# PROGRAMA PRINCIPAL
codigo = "9788535914849"

emprestar_livro(biblioteca, codigo)
devolver_livro(biblioteca, codigo)