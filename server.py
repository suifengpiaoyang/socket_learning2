import socket

"""
The first version : use socket blocking
"""

address = ('127.0.0.1',9999)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(address)
sock.setblocking(False)
sock.listen(5)
client_list = []
print('Waitting for client connect...')

while True:
    try:
        client,addr = sock.accept()
        client_list.append(client)
        client.setblocking(False)
        print('Connected from {}'.format(addr))
    except BlockingIOError:
        pass

    tmp_client_list = [line for line in client_list]
    if len(tmp_client_list) != 0:
        for client in tmp_client_list:
            data = client.recv(1024)
            print('Recved data 【{}】 from {}'.format(data,addr[0]))
            client.sendall(data)
            print('Send data【{}】 to the client.'.format(data))
            client.close()
            client_list.remove(client)
    else:
        pass
