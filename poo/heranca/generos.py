from typing import List
from abc import abstractmethod

class Animal:
    pass

class Mamifero(Animal):
    pass

class Ave(Animal):
    cores: List[str] = None
    altura: int = None # Em cm
    peso: int = None # Em g

    @abstractmethod
    def comer(self):
        print('comendo')

    def dormir(self):
        print('dormindo')
