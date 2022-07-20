from argparse import ArgumentParser

parser = ArgumentParser(prog='ShellTests', # Nome do programa
                        usage='ShellTests [arg]', # Como usar o programa
                        description='''\n
                        Mensagem do help''', # Mensagem do help
                        epilog='Entendeu?', # Mensagem após os parametros
                        fromfile_prefix_chars='@') # $ python test.py @file.txt | Arquivos com os parâmetros pré-fixados

# Argumentos obrigatórios:
#parser.add_argument('x')
#parser.add_argument('y')

# Argumentos opcionais:
#parser.add_argument('-f')
parser.add_argument('-b', '--bar', action='append', dest='xpto')

# Actions:
# None -> salva argumento
# append -> Adiciona na lista
# count -> Conta qtas vzs o argumento foi chamado (-vvvv retorna v=4)

# const -> define um tipo (const=int) (const=str) | a flag não recebe nenhum valor
# default -> Altera o default de None para o que eu definir (default=10)
# type -> define o tipo do argumento (type=int)
# choices -> Não permite que o argumento tenha um valor diferente do definido na lista (choices=['1', '2', '3']) ou (type=int, choices=[1, 2, 3])
# required -> Obriga a usar um argumento (required=True)
# help -> Descrição do que o argumento faz
# metavar -> Nome da variavel
# dest -> Adiciona lista em uma variável

args = parser.parse_args()
print(args)

#parser.print_help()

