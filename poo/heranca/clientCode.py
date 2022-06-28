from mamiferos import *
from aves import *
from ornitorrinco import Ornitorrinco

if __name__ == '__main__':
    # Mamíferos
    pateta = Cachorro(200, 30_000)
    perna_longa = Coelho(40, 1_500)
    frajola = Gato(50, 4_000)
    gaguinho = Porco(150, 90_000)

    print('Frajola')
    frajola.comer()
    frajola.comer()
    frajola.pararDeComer()
    frajola.locomoverSe()

    print('\nPateta')
    pateta.dormir()
    pateta.latir()
    pateta.locomoverSe()

    # Aves
    joao = Frango(30, 2_500, ['Amarelo'])
    pica_pau = PicaPau(35, 250, ['Vermelho', 'Azul', 'Branco'])
    patolino = Pato(60, 1_200)
    zeca_urubu = Urubu(65, 1_500)

    print('\nPica-Pau')
    pica_pau.locomoverSe()
    pica_pau.botarOvos()
    pica_pau.bicar()

    # Bagulhos estranhos
    # print('\nPerry')
    # perry = Ornitorrinco(50, 1_800)
    # perry.som()
    # perry.botarOvos()
    # perry.amamentar()
