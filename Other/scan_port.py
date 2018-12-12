# encoding:utf-8

import socket, threading, time
from redis import StrictRedis

success_list = []
socket.setdefaulttimeout(0.5)  # 设置socker超时，单位秒


def get_port_status(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_DGRAM是udp协议,STREAM是tcp协议

    try:
        server.connect((ip, port))
        # print('%s的端口号%s可用'%(str(ip),str(port)))
        success_list.append(ip)
    except Exception as e:
        # print(server.getsockname()[0])
        pass
    finally:
        server.close()


def start_redis(ip):
    try:

        r = StrictRedis(host=ip, socket_timeout=0.1)
        info = r.set('name', 'systemclt')
        if info is True:
            print('\033[0;33;44m 发现肉鸡：\033[0m', ip)

    except:
        pass


if __name__ == '__main__':
    start_ip = '192.168.1.'
    for end_ip in range(1, 254):
        ip = start_ip + str(end_ip)
        t1 = threading.Thread(target=get_port_status, args=(ip, 6379))
        t1.start()
    time.sleep(1)

    for data in success_list:
        start_redis(data)
    print('结束~')
