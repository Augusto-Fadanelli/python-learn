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