from socket import *
import threading

# Create a UDP socket
local_socket = socket(AF_INET, SOCK_DGRAM)

def receiveMessage():
    while True:
        data, server = local_socket.recvfrom(4096)
        print(f'Resposta: {data}')

def sendMessage(server_address):
    while True:
        message = input()
        sent = local_socket.sendto(message.encode(), server_address)

if __name__ == '__main__':
    server_port = 12000
    while True:

        server_ip = input('Digite o IP: ')
        server_address = (server_ip, server_port)

        threading.Thread(target=receiveMessage).start()
        sendMessage(server_address)
