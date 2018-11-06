#enconding:utf-8

import socket,os,zipfile,requests,time
def get_host_ip():
    '''发起udp协议进程，获取本机 IP'''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('1.1.1.1', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def download_zabbix():
    '''从zabbix下载agent_3.4.6版'''
    try:
        url = "https://www.zabbix.com/downloads/3.4.6/zabbix_agents_3.4.6.win.zip"
        r = requests.get(url)
        with open ("zabbix.zip","wb") as f:
            f.write(r.content)
        return 0
    except Exception as e:
        print(e)
        return 1

def unzip():
    '''把下载的孙佳佳，进行高度解压，然后放在D盘'''
    try:
        f = zipfile.ZipFile('zabbix.zip')
        for file in f.namelist():
            f.extract(file, 'c:/Program Files/zabbix agent/')
        return 0
    except Exception as e:
        print(e)
        return 1


def write_config(config):
    with open('c:\Program Files\zabbix agent\conf\zabbix_agentd.win.conf','w+') as f:
        for conf in config:
            f.write(conf)


def install_zabbix():
    '''安装zabbix，并启动撒'''
    try:
        os.chdir('c:/Program Files/zabbix agent/bin/win64')
        os.system('.\zabbix_agentd.exe -c "c:/Program Files/zabbix agent/conf/zabbix_agentd.win.conf" -i')
        os.system('.\zabbix_agentd.exe -c "c:/Program Files/zabbix agent/conf/zabbix_agentd.win.conf" -s')
        return 0
    except Exception as e:
        print(e)
        return 1


ip =get_host_ip()
config = ('''ServerActive=%s
Server=%s
StartAgents=5
Hostname=%s
DebugLevel=3
LogFile=c:\Program Files\zabbix agent\zabbix_agentd.log
Timeout=3''') % ('10.0.7.38', '10.0.7.38',ip)

if __name__ == '__main__':
    print('正在从zabbix官网下载zabbix-agent...')
    dw= download_zabbix()

    if dw ==0:
        print('解压文件...')
        zi = unzip()
        if zi == 0:
            print('修改配置...')
            write_config(config)
            print('卧槽，小佳佳要自爆啦...\n 系统将在3秒后退出！')
            install_zabbix()
            print('为孙佳佳服务的强强，麻麻咪')
            time.sleep(3)

    else:
        exit(0)