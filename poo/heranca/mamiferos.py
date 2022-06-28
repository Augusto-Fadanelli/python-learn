from generos import Mamifero

class Cachorro(Mamifero):
    def __init__(self, tam: int, peso: int):
        super().__init__(tam, peso, True)

    def latir(self):
        print('\tAu au au!')

class Coelho(Mamifero):
    def __init__(self, tam: int, peso: int):
        super().__init__(tam, peso, False)

    def fugir(self):
        print('\tO coelho fugiu!')

class Gato(Mamifero):
    def __init__(self, tam: int, peso: int):
        super().__init__(tam, peso, True)

    def miar(self):
        print('\tMiau!')

class Porco(Mamifero):
    def __init__(self, tam: int, peso: int):
        super().__init__(tam, peso, True)

    def grunhir(self):
        print('\tOinc!')