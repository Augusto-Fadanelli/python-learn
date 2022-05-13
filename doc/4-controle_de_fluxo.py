# for
'''
users = {'Hans': 'active', 'Éléonore': 'inactive', 'Augusto': 'active'}
print(users)

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)
'''

# range()
'''
for i in range(5):
    print(i)

print()

for i in range(2, 8):
    print(i)

print()

for i in range(0, 10, 3):
    print(i)

print()

text = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(text)):
    print(i, text[i])

print()

print(sum(range(4)))
print(sum(range(0,100,2)))
'''

# enumerate()
'''
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for i in enumerate(seasons, start=2):
    print(i)
'''

# match
'''
status = input('Informe o status: ')
match status:
    case '400':
        print('Bad request')
    case '404':
        print('Not found')
    case '418' | '419' | '420':
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")
'''

# in
# Uma maneira elegante de verificar strings digitadas:
'''
def ask_ok(prompt, retries=2, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)
        print(f'Tentativas restantes: {retries+1}')


if ask_ok('Continue? (yes|nope)'):
    print('Loading...')
'''

# def
# listas, dicionários e instâncias de classes acumulam os argumentos passados nas chamadas subsequentes
'''
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
'''
# Para que isso não ocorra pode ser escrito assim
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))



### Parei em 4.8.2 ###


