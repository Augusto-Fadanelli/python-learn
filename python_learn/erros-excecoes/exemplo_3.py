# Criar meus erros

class MeuErro(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f'Meu erro foi pensar que o flamengo é time. {self.msg}'

raise MeuErro('O flamengo é seleção!')
