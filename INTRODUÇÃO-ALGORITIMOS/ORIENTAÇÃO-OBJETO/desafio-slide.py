class Cliente:
    #CONTRUCTOR
    def __init__(self,x,y):
        self.nome = x
        self.matricula = y

    #FUNÇÃO DE EXIBIÇÃO    
    def exibir(self):
        print(f"Cliente: {self.nome} \nMatricula: {self.matricula}")

class Produto:
    def __init__(self,x,y):
        self.nome = x
        self.preco = y

    def exibir(self):
        print(f"Produto: {self.nome} \nPreço: {self.preco}")

class itemPedido:
    def __init__(self,produto,quantidade):
        self.produto = produto
        self.quantidade = quantidade
    
    #COMO APENAS CALCULA ELE NÃO RECEBE PARAMETROS
    def calcular_subtotal(self):
        return self.produto.preco * self.quantidade
    
    def exibir(self):
        print(f"Produto:{self.produto.nome} Preço:{self.produto.preco}  Quantidade:{self.quantidade}")

#MAIN
p1 = itemPedido("Pizza",10.00,1)
p1.exibir()




