#!/usr/bin/env python

"""
Created by Zzq_OPS.
Env:         python2.
File:        install zabiix-agent4.0.
User:        zzq.
Create Date:    2019-04-09.
 """

import os

def Check_System_Version():
    cmd = "cat /etc/centos-release |awk '{print$4}' |awk -F. '{print$1}'"
    result = os.popen(cmd).read().strip('\n')
    if int(result) != 7:
        print 'The script currently only supports centos7. Please confirm the system.'
        return 1
    elif int(result) == 7:
        return 0
    else:
        print 'Unknown Error'
        return 2

def Check_Software_Installation():
    cmd = 'rpm -qa|grep zabbix-agent'
    result = os.popen(cmd).read().replace('\n',"")
    if result == "":
        return 0
    else:
        print result,'is already installed'
        return 1

def Install_Zabbix_Agent(conf):
    rpm = 'rpm -Uvh https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm'
    yum = 'yum -y install zabbix-agent'
    os.system(rpm)
    os.system(yum)
    if Check_Software_Installation() == 1:
        with open('/etc/zabbix/zabbix_agentd.conf','w') as f:
            f.write(conf)
        os.system('systemctl enable zabbix-agent')
        os.system('systemctl start zabbix-agent')
        print 'zabbix agent install success, Please login to zabbix-server for follow-up action \n Good bye!'
    elif Check_Software_Installation() == 0:
        print 'install faild'
        exit(1)

if __name__ == '__main__':
    if Check_System_Version() == 0 and Check_Software_Installation() == 0:
        hostname = raw_input("Please enter hostname =>")
        server_ip = raw_input("Please enter zabbix server ip =>")
        conf = '''PidFile=/var/run/zabbix/zabbix_agentd.pid
        LogFile=/var/log/zabbix/zabbix_agentd.log
        LogFileSize=0
        StartAgents=0
        Hostname={}
        ServerActive={}        
        RefreshActiveChecks=120'''.format(hostname,server_ip)
        Install_Zabbix_Agent(conf)
    else:
        exit(1)


