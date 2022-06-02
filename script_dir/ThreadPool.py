'''使用线程池'''

from socket import AF_INET,SOCK_STREAM,socket
from concurrent.futures import ThreadPoolExecutor

def echo_client(sock,client_addr):
    '''handle a client connction
    '''
    print('Got connection from ',client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('client closed connection')
    sock.close()

def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock,client_addr = sock.accept()
        pool.submit(echo_client,client_sock,client_addr)

echo_server(('127.0.0.1',20000))
