import socket

address = ('127.0.0.1',9999)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(address)
sock.sendall(b'test')
data = sock.recv(1024)
print('Recvd data 【{}】 from server.'.format(data))
sock.close()
