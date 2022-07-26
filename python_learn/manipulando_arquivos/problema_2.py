import os
import os.path
import shutil
from pathlib import Path

# Cria arquivos
for elemento in range(1, 11):
    Path(f'live_{elemento}.txt').touch()

# Lista arquivos que começam com live_
l = [ f for f in os.listdir('.') if f.startswith('live_') ]
print(f'Arquivos criados:\n{l}')

# Remove arquivos que terminam menores que 6
for _file in l:
    if int(_file.partition('_')[2][0]) <= 5: # Utilizando regex ficaria mais legível
        os.remove(_file)

# Lista arquivos novamente
l = [ f for f in os.listdir('.') if f.startswith('live_') ]
print(f'Arquivos atuais:\n{l}')

for val, elemento in enumerate(sorted(l), 1):
    shutil.move(elemento, f'live_{val}')

# Lista arquivos novamente
print('Novos nomes:')
print([ f for f in os.listdir('.') if f.startswith('live_') ])


