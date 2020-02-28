import select
import socket

"""
The first version : use socket blocking
The second version : use socket nonblocking
The third version : use select
"""

address = ('127.0.0.1', 9999)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(address)
server.setblocking(False)
server.listen(5)
input = [server]
print('Waitting for client connect...')

while True:

    readable, _, _ = select.select(input, [], [])

    for sock in input:
        if sock is server:
            client,addr = sock.accept()
            print('Connected from {}'.format(addr))
            client.setblocking(False)
            input.append(client)
        else:
            data = sock.recv(1024)
            print('Recved data 【{}】 from {}'.format(data, sock.getpeername()))
            sock.sendall(data)
            print('Send data【{}】 to the client.'.format(data))
            sock.close()
            input.remove(sock)
