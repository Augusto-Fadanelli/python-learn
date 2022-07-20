class TestError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

    @staticmethod
    def batatinhas():
        return 'batatinhas'

if __name__ == '__main__':
    try:
        print('Dentro do try.')
        raise TestError('Erro de teste.')
    except TestError as test:
        print('Dentro do except.')
        print(test.batatinhas())
