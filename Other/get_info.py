#encoding:utf-8
import os,socket
# task =os.popen("vmstat | awk 'NR==3''{print$12}'").read() #获取进程数
# use = os.popen("vmstat | awk 'NR==3''{print$15}'").read()
# men = os.popen("free  |awk 'NR==2'{'printf $3/$2'}").read()
# cpu_use = '%0.2f%%'%(100.00 - float(use))  #获取cpu使用率
# men_use = '%0.2f%%'%(float(men)*100)       #获取menory使用率
# mysql_max_con = "mysqladmin -uroot -proot variables |grep  max_connections|awk 'NR==2''{print$4}'" #mysql最大连接数
# mysql_con = "mysqladmin -uroot -proot status |awk '{print$4}'"  #mysql当前连接数
# try:
#     print ('mysql连接数:%d/%d'%(int(mysql_con),int(mysql_max_con)))
# except:
#     pass

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