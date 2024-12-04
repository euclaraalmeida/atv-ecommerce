from product import Produto
from item_pedido import ItemPedido
from pilha_encadeada import *

pilha=Pilha()
class Pedido:
    def __init__(self, id:int):
        self.id = id # id do pedido
        self.itens = []# dicionario com os itens de pedido
    
    def adicionar_item(self, produto:Produto, quantidade:int):
        self.itens.append(ItemPedido(produto, quantidade))

    def total_pedido(self):
        total = 0
        for item in self.itens:
            total += item.total_item()
        return total
    
    def mostrar_carrinho(self):
        print('======================================================')
        print("                 Itens do pedido:")
        print('======================================================')
        print('idProduto  | Descrição      | Preço Unit. | Quantidade ')
        print('-----------  ---------------  ------------  ----------')
              
        for item in self.itens:
            pilha.empilha(item)
        
    
        for item in self.itens:
            elem = pilha.desempilha()
            print(f'    {elem.produto.id:03d}      {elem.produto.descricao:15s}     {elem.produto.valor:9.2f}      {elem.quantidade:3d}')
            
        print('======================================================')
        print(f"Valor total das suas comprinhas: R$ {self.total_pedido():.2f}")
        print('======================================================')
    
    def __str__(self):
        return f"Pedido: {self.id} | Total: {self.total_pedido():.2f}"