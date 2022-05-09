from socket import *
from pickle import dumps

if __name__ == '__main__':
    numbers = []

    i = 0
    while True:
        n = input(f'Informe o {i+1}º número (end para finalizar): ')
        numbers.append(n)

        if numbers[i] == 'end':
            del numbers[i]
            break

        numbers[i] = int(numbers[i])
        i += 1

    # Create a UDP socket
    local_socket = socket(AF_INET, SOCK_DGRAM)
    server_port = 12000

    server_ip = input('Digite o IP: ')
    server_address = (server_ip, server_port)

    data = dumps(numbers)
    local_socket.sendto(data, server_address)