'''接收时间服务器的时间'''
from socket import socket,AF_INET,SOCK_STREAM
s = socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',12000))
print(s.recv(1024).decode('utf-8'))
s1 = socket(AF_INET,SOCK_STREAM)
s1.connect(('127.0.0.1',11000))
print(s1.recv(1024).decode('utf-8'))
