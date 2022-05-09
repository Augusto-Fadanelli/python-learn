from socket import *

if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_port = 12000
    server_socket.bind(('', server_port))
    print(f'Iniciando servidor na porta {server_port}.')

    name = 'Ben Tennyson'
    while True:
        print(f'Esperando nome {name}...')
        n, address = server_socket.recvfrom(4096)
        n = n.decode("utf-8")

        if n == name:
            print('Nome correto.')
        else:
            print(f'{n} não é {name}.')
