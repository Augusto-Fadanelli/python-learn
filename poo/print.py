#######################################
#          Escopo de classse          #
#######################################
class Impressora:
    mensagem = 'Folha impressa'

    @classmethod
    def imprimirFolha(cls):
        print(cls.mensagem)

    @classmethod
    def imprimirLivro(cls, qtd_fohas):
        for i in range(qtd_fohas):
            cls.imprimirFolha()

if __name__ == '__main__':
    Impressora.imprimirFolha()
    print()
    Impressora.imprimirLivro(5)
    print()
    imp = Impressora()
    imp.imprimirFolha()

#######################################
#         Escopo de instancia         #
#######################################

class Impressora:
    # mensagem = 'Folha impressa'
    def __init__(self):
        self.mensagem = 'Folha impressa'
    ###

    # @classmethod
    # def imprimirFolha(cls):
    #     print(cls.mensagem)
    def imprimirFolha(self):
        print(self.mensagem)
    ###

    def imprimirLivro(self, qtd_fohas):
        for i in range(qtd_fohas):
            self.imprimirFolha()

if __name__ == '__main__':
    imp = Impressora()
    imp.imprimirFolha()
    print()
    imp.imprimirLivro(5)

    # print()
    # Impressora.imprimirFolha()