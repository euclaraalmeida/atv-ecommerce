from product import Produto
class ItemPedido:
    def __init__(self, produto:Produto, quantidade:int):
        self.produto = produto
        self.quantidade = quantidade

    def total_item(self):
        return self.produto.valor * self.quantidade
    
    def __str__(self):
        return f"{self.produto.descricao} | Quantidade: {self.quantidade} | Total: {self.total_item():.2f}"