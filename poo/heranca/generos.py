from typing import List
from abc import ABC, abstractmethod

class Animal(ABC):
    __dormindo = False
    __comendo = False

    def __init__(self, tam: int, peso: int):
        self.tam = tam
        self.peso = peso

    def dormir(self):
        if self.__dormindo:
            print('\tJá está dormindo.')
        else:
            self.__dormindo = True
            print('\tFoi dormir.')

    def acordar(self):
        if self.__dormindo:
            self.__dormindo = False
            print('\tAcordou.')
        else:
            print('\tJá está acordado.')

    def comer(self):
        if self.__comendo:
            print('\tJá está comendo.')
        else:
            self.__comendo = True
            print('\tComeçou a comer.')

    def pararDeComer(self):
        if self.__comendo:
            self.__comendo = False
            print('\tTerminou de comer.')
        else:
            print('\tNão está comendo.')

    @abstractmethod
    def locomoverSe(self) -> None:
        pass

class Mamifero(Animal):
    def __init__(self, tam: int, peso: int, carnivoro: bool):
        super().__init__(tam, peso)
        self.carnivoro = carnivoro

    def locomoverSe(self):
        print('\tEstá andando.')

    def amamentar(self):
        print('\tAmamentou a prole.')

class Ave(Animal):
    def __init__(self, tam: int, peso: int, cores: List[str]=['Preto']):
        super().__init__(tam, peso)
        self.cores = cores

    def locomoverSe(self):
        print('\tEstá voando.')

    def botarOvos(self):
        print('\tBotou Ovos.')