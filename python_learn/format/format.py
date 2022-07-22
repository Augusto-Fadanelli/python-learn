pessoa = {
        'nome': 'Augusto',
        'idade': 18,
        'apelido': 'Fadanelli'
        }

s = 'Oi {nome}, vi que tem {idade} anos e seu apelido é {apelido}'

print(s.format(**pessoa))
