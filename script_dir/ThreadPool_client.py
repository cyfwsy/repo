'''Tcp 的客户端'''
from socket import AF_INET,SOCK_STREAM,socket
def main(num_clients):
    for i in range(num_clients):
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect(('127.0.0.1',20000))
        text = '中文信息---information'.encode('utf-8')
        sock.send(text)
        ret_value = sock.recv(1024)
        # print(ret_value)
        print(ret_value.decode('utf-8'))

if __name__ == '__main__':
    main(5)
