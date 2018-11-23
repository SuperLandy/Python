# coding utf8
import os,time
import sys
start_Time = int(time.time())
ip_True = open('ip_True.txt','w+')
ip_False = open('ip_False.txt','w+')
IPhost = []
IPbegin = input(u'start_IP： ')
IPend = input(u'stop_IP： ')
IP1 =  IPbegin.split('.')[0]
IP2 =  IPbegin.split('.')[1]
IP3 =  IPbegin.split('.')[2]
IP4 =  IPbegin.split('.')[-1]
IPend_last = IPend.split('.')[-1]
count_True,count_False = 0,0
for i in range(int(IP4)-1,int(IPend_last)):
     ip = str(IP1+'.'+IP2+'.'+IP3+'.'+IP4)
     int_IP4 = int(IP4)
     int_IP4 += 1
     IP4 = str(int_IP4)
     return1=os.system('ping -n 1 -w 1 %s'%ip)
     if return1:
         print ('ping %s is fail'%ip)
         ip_False.write(ip+'\n')
         count_False += 1
     else:
         print ('ping %s is ok'%ip)
         ip_True.write(ip+'\n')
         count_True += 1
ip_True.close()
ip_False.close()
end_Time = int(time.time())
print ("time(s)：",end_Time - start_Time,"s")
print ("ping success ip count：",count_True,"   ping faild ip count：",count_False)
