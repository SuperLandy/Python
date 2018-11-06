#ecoding:utf-8
import time,os
def timer():
    start_time=time.time()
    suanfa()
    stop_time=time.time()
    print('run time is %s秒'%(stop_time-start_time))

def suanfa():
    a = os.popen('ping www.baidu.com')
    print(a.read())
    # if a == 0:
    #     print('命令执行成功！！')
    # else:
    #     print('命令执行失败.')

timer()




