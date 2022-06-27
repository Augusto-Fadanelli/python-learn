class Switch:
    ligado = False

    @staticmethod
    def toggle():
        #cls.ligado = not cls.ligado
        print('sla')

    @classmethod
    def getState(cls):
        return cls.ligado

def clientCode():
    if Switch.getState():
        print('Ligado')
    else:
        print('Desligado')

if __name__ == '__main__':
    clientCode()

    Switch.toggle()
    clientCode()