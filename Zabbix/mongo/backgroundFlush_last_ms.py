#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,json

def get_network(host,user,password):
    _cmd = 'mongo {} -u{} -p{} --authenticationDatabase admin --eval "printjson(db.serverStatus().backgroundFlushing.last_ms)"|awk "NR==3"'.format(host,user,password)
    try:
        result = os.popen(_cmd).read().strip('\n')
        print round(float(result),3)  #最后一次写磁盘的耗时,取小数点后三位,ms毫秒
    except EOFError as err:
        print err

if __name__ == '__main__':
    host= '192.168.91.83:27017'
    user='root'
    password='pass'
    get_network(host,user,password)
