import socket

"""
The first version : use socket blocking
"""

address = ('127.0.0.1',9999)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(address)
sock.listen(5)
print('Waitting for client connect...')

while True:
    s,addr = sock.accept()
    print('Connected from {}'.format(addr))
    data = s.recv(1024)
    print('Recved data 【{}】 from {}'.format(data,addr[0]))
    s.sendall(data)
    print('Send data to the client.')
    s.close()
