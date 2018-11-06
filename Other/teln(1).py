import time
import telnetlib
def timer():                                                            #对程序运行耗时统计
    start_time=time.time()
    runtelnet(host,username,passwd,finsh,commands)                        # telnet脚本
    stop_time=time.time()
    print('本次操作共耗时%d秒，小佳佳为你点赞!'%(stop_time-start_time))

def runtelnet(host,username,passwd,finsh,commands):    #telnet远程登录
    tln = telnetlib.Telnet(host,port=23,timeout=3)
    tln.set_debuglevel(2)
    tln.read_until('\r\nUsername:'.encode())                       #用户名，避免错误延时3秒执行下一个命令
    tln.write(username.encode('ascii') + b'\n')
    time.sleep(2)
    tln.read_until('\r\nPassword:'.encode())                                      #输入密码，避免错误延时3秒执行下一个命令
    tln.write(passwd.encode('ascii') + b'\n')
    time.sleep(2)
    if tln.expect(finsh.encode()):
        for cmd in commands:
            print('登录成功，现在开始配置路由器！！！')
            tln.write(cmd.encode('ascii') + b'\n')
        tln.read_until(done.encode())                               #匹配到finsh时候关闭telnet
        print('配置成功并已生效')
        tln.close()
if __name__ =='__main__':                           #定义IP，用户名，密码等信息
    print('该脚本基于python3开发,目前只支持华三、华为路由器及交换机!')
    host     =     input('路由器IP地址:')
    username =     input('路由器用户名:')
    passwd   =     input('路由器密码:')
    finsh    =     ('>')                              #定义开始登录成功提示符号
    done     =     (']')                              #定义命令结束提示符合
    commands =     ['sys','dis cur']                #配置命令在此输入
    timer()
 #