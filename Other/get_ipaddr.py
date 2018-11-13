import socket,os
from urllib import request
server = socket.socket()
server.bind(('192.168.1.29',6666,))
list = []
for i in range(1):
    server.listen()
    print('wating.....')
    con,ipadd = server.accept()
    date = con.recv(10000).decode()
    list.append(date)
    i = i+1
server.close()
print(list)