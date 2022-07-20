from os.path import exists

def read_file(file):
    if not exists(file):
        raise FileNotFoundError(f'O arquivo {file} não existe.') # Exibe uma exceção

read_file('bananas.txt')
