#!/usr/bin/env python
#enconding:utf-8
import pika
credential = pika.PlainCredentials('zzq','123456') #robbit_user,password
connection =pika.BlockingConnection(pika.ConnectionParameters(host='192.168.91.85',credentials=credential))
channel =connection.channel()

def callback(ch,method,properties,body):
    print('revice message is ',body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  #消息确认被消费
def consume():
    channel.queue_declare(queue='woshitiancai',durable=True) #开启durable 队列持久化
    channel.basic_consume(on_message_callback=callback,
                          queue='woshitiancai')
    channel.start_consuming()
channel.basic_qos(prefetch_count=1) #最大消息处理量
consume()

