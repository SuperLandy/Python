#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,json

def get_network(host,user,password):
    _cmd = 'mongo {} -u{} -p{} --authenticationDatabase admin --eval "printjson(db.serverStatus().connections.current)"|awk "NR==3"'.format(host,user,password)
    try:
        result = os.popen(_cmd).read().strip('\n')
        print result
        #result = json.loads(result)
        #connection_current = result.get('current')  
        #print connection_current
    except EOFError as err:
        print err

if __name__ == '__main__':
    host= '192.168.91.83:27017'
    user='root'
    password='pass'
    get_network(host,user,password)
