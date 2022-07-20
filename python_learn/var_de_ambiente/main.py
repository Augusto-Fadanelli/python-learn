# Aula: https://youtu.be/DiiKff1z2Yw
# Lives úteis: #97 e #104

from os import environ

print(environ['USER'])
print(environ['LANG'])
print(environ['HOME'])
print(environ['MAIL'])

# Printa todas as variáveis de sistema
#print(list(environ))

# Mais seguro pois não retorna um erro quando não encontra a variável
print(environ.get('LDP'))
print(environ.get('LDP', 'teste')) # Se não existir retorna 'teste'

# define uma variável de sistema
environ['LDP'] = 'Batata Palha'

print(environ.get('LDP', 'Não vai mostrar isso'))


# Outra forma. Aqui tem uma diferença, getenv não põe os valores retornados em memória. Isso pode ser mais seguro.
from os import getenv

print(getenv('XPTO', 'abc'))
print(getenv('LDP', 'teste123'))
# Não existe setenv()


#### Usar variáveis de ambiente com .env ####

# Entrar na virtual env

# Criar arquivo .env e adicionar as variáveis de ambiente
# SUA_KEY="alguma coisa"
# OUTRA_KEY="/home/hanno/thumb/pokedex.png"

# pip install python-dotenv

# from os import getenv
# from dotenv import load_dotenv
# load_dotenv()
# getenv('SUA_KEY')

# Mostrar todas as variaveis de ambiente em .env
# dotenv_values()
