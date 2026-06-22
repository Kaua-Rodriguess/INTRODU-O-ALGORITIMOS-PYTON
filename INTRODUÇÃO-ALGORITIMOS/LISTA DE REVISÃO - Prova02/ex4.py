isbn = {
    "titulo": "platão",
    "autor": "socrates",
    "qtd_estoque": "10"
}

def emprestar_livro(isbn):
    
    #verifica se há ou não
    if "qtd_estoque" in isbn:
        isbn["qtd_estoque"] -= 1
        print("Livro emprestado!")
    else:
        print("Não ha livro em estoque!")

#def devolver_livro(isbn):