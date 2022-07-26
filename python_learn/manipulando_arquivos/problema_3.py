import os
import os.path
import shutil
from pathlib import Path

# Cria 10 pastas
for x in range(1, 11):
    dir_ = f'pasta_{x}'
    if not os.path.exists(dir_):
        os.mkdir(dir_)

# Lista pastas
l = [path for path in os.listdir('.') if os.path.isdir(path)]
print(f'Patas criadas:\n{l}')

# Cria arquivos nas pastas
for path in l:
    Path(os.path.join(path, 'arquivo_1.txt')).touch()
    Path(os.path.join(path, 'arquivo_2.txt')).touch()

# Junta tudo
#print(os.path.join('/', 'Live', 'Python', 'xpto.txt'))

# Mostra árvore de diretórios
print('\nÁrvore de diretórios:')
for val in os.walk('.'):
    print(val)

