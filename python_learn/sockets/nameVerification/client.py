from socket import *

if __name__ == '__main__':
    name = input('Informe o nome: ')

    local_socket = socket(AF_INET, SOCK_DGRAM)
    server_port = 12000

    server_ip = input('Digite o IP: ')
    server_address = (server_ip, server_port)

    local_socket.sendto(name.encode(), server_address)
