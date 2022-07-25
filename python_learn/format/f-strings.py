from datetime import datetime

nome = 'Augusto'

print(f'{nome.upper()}')

print(f'{"Ração"!s}') # Chama string | É o mesmo que não colocar nada
print(f'{"Ração"!r}') # Chama a representação
print(f'{"Ração"!a}') # Converte o texto pra ASCII

print(f'{nome=}') # Saída: nome='Augusto'

produto = 'Ração'
print(f'{produto.upper()=!a}') # Misturando as coisas

# {:[preenchimento][alinhamento][tamanho_mínimo]}
print(f'{"Ração":20} {"Augusto":10}')

# Ex.: Tamanho
nomes = ['Augusto', 'Eduardo', 'Nietzsche']
idades = [22, 29, 100]

for nome, idade in zip(nomes, idades):
    print(f'{nome:12} {idade:5}')

# Ex.: Alinhamento
# < Esquerda | > Direita | ^ Centro
for nome, idade in zip(nomes, idades):
    print(f'{nome:>12} {idade:<5}')

# Ex.: Preenchimento
print(f'{" Menu ":-^30}') # preenchimento
print(f'{"| 1 - Opção um":<29} {"|"}')
print(f'{"| 2 - Opção dois":<29} {"|"}')
print(f'{"| 3 - Opção três":<29} {"|"}')
print('-'*30)

# Datas
agora = datetime.now()
print(agora)
print(f'{agora:%d/%m/%Y %Hhrs %Mmin %Ssec}')
