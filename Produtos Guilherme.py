class Produtos:
    def __init__(self, nome, preço, estoque, categoria):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque
        self.categoria = categoria


    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preço:.2f}")
        print(f"Estoque: {self.estoque}")


    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço: {self.preço}:.2f")
        print(f"Estoque: {self.estoque}")


    def valor_total(self):
        return self.preço * self.estoque


    def aplica_desconto(self, percentual):
        self.preço *= (1-percentual / 100)
        print(f"Desconto aplicado! Novo preço: R$ {self.preço}")


    def vender(self, quantidade):
        if quantidade > self.estoque:
            print("Estoque insuficiente!")
        else:
            self.estoque -= quantidade
            print(f"Vendido {quantidade} x {self.nome}.Estoque restante: {self.estoque}")


    def repor_estoque(self, quantidade):
        self.estoque += quantidade
        print(f"Novo estoque: {self.estoque}")