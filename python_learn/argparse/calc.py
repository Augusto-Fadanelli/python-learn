from argparse import ArgumentParser

parser = ArgumentParser(prog='Calculadora',
                        description='Olá bb, isso é uma calculadora.',
                        fromfile_prefix_chars='@')

parser.add_argument('operação', type=str, help= 'Como vc gostaria de usar?')
parser.add_argument('x', type=int, help='Primeiro valor')
parser.add_argument('y', type=int, help='Segundo valor')
parser.add_argument('-v', action='count', help='Entenda o que estamos fazendo.')

args = parser.parse_args()

# decorator
def verbose(func):
    def _inner(x, y):
        if args.verbose == 1:
            print(f'Estamos operando com {x} e {y}')
        if args.verbose == 2:
            print(f'{func.__name__}({x} e {y})')
        if args.verbose >= 10:
            print('Vá se danar com tanta verbosidade!')
            exit()
        return func(x, y)
    return _inner

@verbose
def soma(x, y):
    return x + y

@verbose
def subt(x, y):
    return x - y

@verbose
def divi(x, y):
    return x / y

@verbose
def mult(x, y):
    return x * y

if __name__ == '__main__':
    operacoes = {'soma': soma,
                 'subtração': subt,
                 'divisão': divi,
                 'multiplicação': mult}

    print(operacoes[args.operação](args.x, args.y))

