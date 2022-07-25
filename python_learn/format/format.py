from math import pi

pessoa = {
        'nome': 'Augusto',
        'idade': 18,
        'apelido': 'Fadanelli'
        }

s = 'Oi {nome}, vi que tem {idade} anos e seu apelido é {apelido}'

print(s.format(**pessoa))

print('{!s}'.format('Ração')) # Chama string | É o mesmo que não colocar nada
print('{!r}'.format('Ração')) # Chama a representação
print('{!a}'.format('Ração')) # Converte o texto pra ASCII

# Conversão de bases
print('{:o}'.format(258761276)) # Octal
print('{:b}'.format(258761276)) # Binário
print('{:x}'.format(258761276)) # Hexadecimal minúsculo
print('{:X}'.format(258761276)) # Hexadecimal maiúsculo
print('{:d}'.format(258761276)) # Decimal

print('{:_^20x}'.format(258761276)) # Juntando tudo

# Casas decimais
print('{:.2f}'.format(pi))
print('{:.^10.2f}'.format(pi))

# Mostrar sinal
print('{:+.2f}'.format(pi))
print('{:+.2f}'.format(-pi))

# Usando format
print(format(pi, '_^20.2f'))
