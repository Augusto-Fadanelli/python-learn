from generos import Mamifero

class Cachorro(Mamifero):
    def latir(self):
        print('\tAu au au!')

class Coelho(Mamifero):
    def fugir(self):
        print('\tO coelho fugiu!')

class Gato(Mamifero):
    def miar(self):
        print('\tMiau!')

class Porco(Mamifero):
    def grunhir(self):
        print('\tOinc!')