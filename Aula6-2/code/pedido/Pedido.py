class Pedido:

    def __init__(self):
        self.valor_total = 0.0
        self.itens_pedido = []

    def adicionar_item(self, item):
        self.itens_pedido.append(item)
        self.valor_total += (item.produto.valor*item.quantidade)

    def obter_total(self):
        return self.valor_total