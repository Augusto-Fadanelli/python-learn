# Aula https://youtu.be/5q-qz3GAj5U

def media_acumulada():
    #import pdb; pdb.set_trace() # Debbuger
    valores = []

    def calcula_media(valor):
        valores.append(valor)
        return sum(valores)/len(valores)

    return calcula_media

if __name__ == '__main__':
    augusto = media_acumulada()
    gustavo = media_acumulada()

    print(augusto(10))
    print(augusto(8))
    print()

    print(gustavo(8))
    print(gustavo(9))
