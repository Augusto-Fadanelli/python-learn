class Pizza:
    pedacos = 8

    def __init__(self, sabor: str):
        self.sabor = sabor

    def getPedaco(self):
        self.pedacos -= 1

    @classmethod
    def mudarTamanho(cls, pedacos: int):
        cls.pedacos = pedacos

    @staticmethod
    def ingredientesBase():
        return 'Massa, molho de tomate, queijo, cebola'

if __name__ == '__main__':
    print(Pizza.pedacos)
    mus = Pizza('Mussarela')
    print(mus.pedacos)
    print()

    mus.getPedaco()
    print(mus.pedacos)
    print(Pizza.pedacos)
    print()

    # Pizza.mudarTamanho(12)
    # print(Pizza.pedacos)
    # print(mus.pedacos)
    #
    # mar = Pizza('Margherita')
    # print(mar.pedacos)

    ###
    # print(Pizza.ingredientesBase())


