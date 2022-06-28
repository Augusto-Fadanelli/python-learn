from typing import List
from abc import abstractmethod

class Animal:
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

class Mamifero(Animal):
    def __init__(self, tam: int, peso: int, carnivoro: bool):
        self.tam = tam
        self.peso = peso
        self.carnivoro = carnivoro

    def comer(self):
        super().comer()

    def dormir(self):
        super().dormir()

class Ave(Animal):
    def __init__(self, tam: int, peso: int, cores: List[str]):
        self.tam = tam
        self.peso = peso
        self.cores = cores

    def comer(self):
        super().comer()

    def dormir(self):
        super().dormir()
