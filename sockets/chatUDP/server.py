from socket import *
import threading

# Create a UDP socket
server_socket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
server_port = 12000
print(f'Iniciando servidor na porta {server_port}')
server_socket.bind(('', server_port))

def receiveMessage():
    while True:
        data, address = server_socket.recvfrom(4096)
        print(f'Resposta: {data}')

def sendMessage(address):
    while True:
        message = input()
        sent = server_socket.sendto(message.encode(), address)

if __name__ == '__main__':
    data, address = server_socket.recvfrom(4096)
    print(f'Resposta> {data}')

    threading.Thread(target=receiveMessage).start()
    sendMessage(address)
