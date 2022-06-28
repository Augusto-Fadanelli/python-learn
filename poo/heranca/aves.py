from generos import Ave

class Frango(Ave):
    def __init__(self, tam: int, peso: int, cores = ['Branco']):
        super().__init__(tam, peso, cores)

    def locomoverSe(self):
        print('\tEstá andando.')

    def cantar(self):
        print('\tCocoricó!')

class PicaPau(Ave):
    def __init__(self, tam: int, peso: int, cores = ['Preto', 'Vermelho']):
        super().__init__(tam, peso, cores)

    def bicar(self):
        print('\tO pica-pau está bicando.')

class Pato(Ave):
    def __init__(self, tam: int, peso: int, cores = ['Preto']):
        super().__init__(tam, peso, cores)

    def nadar(self):
        print('\tO pato está nadando!')

class Urubu(Ave):
    def __init__(self, tam: int, peso: int, cores = ['Preto']):
        super().__init__(tam, peso, cores)

    def voar(self):
        print('\tO urubu está voando!')
