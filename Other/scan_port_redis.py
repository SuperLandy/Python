#!/opt/py3/bin/python3
# encoding:utf-8

import socket, threadpool
from redis import StrictRedis

success_list = []
socket.setdefaulttimeout(0.5)  # 设置socker超时，单位秒

def get_port_status(ip, port=6379):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_DGRAM是udp协议,STREAM是tcp协议
    try:
        server.connect((ip, port))
        success_list.append(ip)
    except:
        pass
    finally:
        server.close()

def start_redis(ip):
    r = StrictRedis(host=ip, socket_timeout=0.5)
    try:
        info = r.set('key', 'values')
        if info is True:
            print('\033[0;33;44m Ok \033[0m')
    except:
        print('false')
        pass



if __name__ == '__main__':
    #start_ip = '39.104.'
    start_ip = str(input('input start ip >>: ')) + '.'
    ip_addr = []
    print("please warit...")
    for three_ip in range(0, 256):
        for end_ip in range(0, 255):
            ip = start_ip + str(three_ip) + '.' + str(end_ip)
            ip_addr.append(ip)             #生成所有ip地址

    pool = threadpool.ThreadPool(1000)
    check_port = threadpool.makeRequests(get_port_status, ip_addr)  # 开启多线程
    for req in check_port:
        pool.putRequest(req)
    pool.wait()                        #等待线程结束

    for data in success_list:       #测试redis
        print(data,end='...')
        start_redis(data)

    print('结束~')
