#!/usr/bin/env python
# coding utf-8
#请叫我天才佳
import os
if os.path.exists('/etc/zabbix'):                              #检查是否已安装zabbix_agent
    print('zabbix_agent已安装，如需xiezai请输入y')
    usechose = input()
    if usechose == 'y':
        os.system('yum -y remove zabbix-agent')
        print('删除成功')
print('创建zabbix用户组')                                      #创建zabbix用户及用户组
usr = os.system('cat /etc/group |grep zabbix')
if usr != 0:
    os.system('groupadd zabbix')
else:
    print('zabbix用户组已存在')
print('创建zabbix用户')
usr1 = os.system('cat /etc/passwd | grep zabbix')
if usr1 != 0:
    os.system('useradd -g zabbix zabbix -s /sbin/nologin')
    print('zabbix用户创建成功 ')
else:
    print('zabbix 用户已存在')
print('导入zabbix源')
                                                                    #配置zabbix源，想要最新的请从官网处查找
yum ='rpm -i http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-release-3.4-2.el7.noarch.rpm'
os.system(yum)
print('导入yum源成功,开始安装zabbix-agent')
os.system('yum -y install zabbix-agent')
print('zabbix-agent已成功安装')
print('下面开始配置zabbix_agentd.conf')
zabbix_server_ip = input('请输入zabbix服务器IP：')
localhostname = input('请输入本机名称：')
os.system('mkdir /var/log/zabbix')
os.system('touch /var/log/zabbix/zabbix_agentd.log')
os.system('chown zabbix:zabbix /var/log/zabbix/zabbix_agentd.log')
f = open('/etc/zabbix/zabbix_agentd.conf', 'w')
f.write("""PidFile=/var/run/zabbix/zabbix_agentd.pid
LogFile=/var/log/zabbix/zabbix_agentd.log
LogFileSize=0
Server=%s
ListenPort=10050
ServerActive=%s
Hostname=%s """ % (zabbix_server_ip,zabbix_server_ip,localhostname))
f.close()
os.system('systemctl enable zabbix-agent')
os.system('systemctl start zabbix-agent')
print('zabbix_agent配置成功')

