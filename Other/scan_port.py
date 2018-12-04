#coding:utf-8

import socket
socket.setdefaulttimeout(0.1)   #设置socker超时，单位秒
def get_port_status(ip,port):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_DGRAM是udp协议,STREAM是tcp协议
    try:
        server.connect((ip,port))
        print('ip：{}的{}端口可用'.format(ip,port))
    except Exception as e:
        print(server.getsockname()[0])
        pass
    finally:
        server.close()

if __name__ == '__main__':
    ip = '8.8.8.8'
    for port in range(20,90):
        get_port_status(ip,port)
