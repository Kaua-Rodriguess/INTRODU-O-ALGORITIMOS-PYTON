#Um sistema de biblioteca utiliza um dicionário onde a chave é o ISBN do livro
#  e o valor é uma lista [Titulo, Autor, Quantidade_Estoque]. Crie funções
#  para emprestar_livro(isbn) (reduz estoque ou avisa se não há) e
# devolver_livro(isbn), que aumenta o estoque do livro devolvido.

isbn = {
    "titulo": "platão",
    "autor": "socrates",
    "qtd_estoque": "10"
}

def emprestar_livro(isbn):

    #verifica se há ou não
    if isbn["qtd_estoque"] < 1:
     print("Não ha livro em estoque!")
    else:
       isbn["qtd_estoque"] -= 1
       print("Livro emprestado!")

    print(f"Quantidade em estoque: {isbn["qtd_estoque"]}")
       
    
def devolver_livro(isbn):
   
   isbn["qtd_estoque"] += 1
   print("Livro devolvido!")

#PROGRAMA PRINCIPAL

print(f"{emprestar_livro (isbn["qtd_estoque"])}")
print(f"{devolver_livro (isbn["qtd_estoque"])}")
