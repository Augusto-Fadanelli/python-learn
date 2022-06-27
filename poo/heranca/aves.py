from generos import Ave

class PicaPau(Ave):
    cores = ['vermelho', 'azul', 'branco']
    altura = 35
    peso = 250

    # def comer(self):
    #     print('comendo')

    # def dormir(self):
    #     print('dormindo')

    def voar(self):
        pass


class Urubu(Ave):
    cores = ['vermelho']
    altura = 65
    peso = 1_200

class PapaLeguas(Ave):
    cores = ['azul', 'roxo']
    altura = 56
    peso = 280