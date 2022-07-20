from generos import Mamifero, Ave

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, tam, peso):
        super().__init__(tam, peso, False)

    def som(self): # Onomatopeia
        print('\tGrrrrr!')