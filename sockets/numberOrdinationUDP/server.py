# É necessário instalar o numpy:
# pip install numpy

from socket import *
from pickle import loads
import numpy as np

if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_port = 12000
    server_socket.bind(('', server_port))
    print(f'Iniciando servidor na porta {server_port}.')

    ordered_numbers = []
    while True:
        print('Esperando vetor de inteiros...')
        numbers, address = server_socket.recvfrom(4096)

        arr = loads(numbers)
        print(np.sort(arr))
