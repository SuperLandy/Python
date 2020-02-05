import pika
import time
credential = pika.PlainCredentials('zzq', '123456')  # robbit_user,password
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.91.85', credentials=credential))
channel = connection.channel()


def production(message='woshigourijia'):
    # durable 队列持久化,消费者端也需开启
    channel.queue_declare(queue='woshitiancai', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='woshitiancai',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2  # delivert_mode 消息持久化
                                        ))
    print('ok')


while True:
    with open('./password.txt', 'r') as file:
        for line in file.readlines():
            arg = (line.strip('\n'))
            production(message=arg)
    time.sleep(0.1)
