class Motor:
    def __init__(self, modelo: str, cilindros: int, potencia: int, velocidade_max: int):
        self.modelo = modelo
        self.cilindros = cilindros
        self.potencia = potencia # Em cavalos
        self.velocidade_max = velocidade_max

class Carro:
    def __init__(self, marca: str, modelo: str, placa: str, cor: str, motor: Motor):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.motor = motor

        self._velocidade = 0

    def acelerar(self):
        if self._velocidade <= self.motor.velocidade_max - 10:
            self._velocidade += 10
            print(f'O carro está a {self._velocidade} Km/h')

    def desacelerar(self):
        if self._velocidade >= 10:
            self._velocidade -= 10
            print(f'O carro está a {self._velocidade} Km/h')

if __name__ == '__main__':
    v8 = Motor('V8 5.2', 8, 85, 200)
    maverick = Carro('Ford', 'Maverick', 'KSH-6429', 'Amarelo', v8)

    maverick.acelerar()
    maverick.acelerar()
    maverick.acelerar()
    maverick.desacelerar()
    maverick.desacelerar()
    maverick.desacelerar()