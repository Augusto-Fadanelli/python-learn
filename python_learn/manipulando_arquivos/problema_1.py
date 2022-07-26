import os
import os.path
import shutil
from pathlib import Path

if os.path.exists('aulinha_1'): # Verifica se o diretório já existe
    print('O Diretório já existe!')
else:
    # Cria diretório
    os.mkdir('aulinha_1')

# Cria arquivo
# f = open('aulinha_1/xpto.txt', 'w')
# f.write('Teste')
# f.close()

# Entra no diretório
os.chdir('aulinha_1')

# Cria arquivo utilizando pathlib
Path('xpto.txt').touch()

# Copia xpto.txt
for elemento in range(1, 4):
    shutil.copy('xpto.txt', f'xpto_{elemento}.txt')

# Mostra path atual
print(os.getcwd())

# Lista arquivos
print(os.listdir('.'))

# Verifica se existem 4 arquivos
try:
    assert len(os.listdir('.')) == 4
    print('Tem 4 arquivos.')
except:
    print('Erro: Tem {} arquivos.'.format(len(os.listdir('.'))))
