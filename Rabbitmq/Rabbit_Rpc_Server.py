#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pika
credential = pika.PlainCredentials('zzq','123456') #robbit_user,password
connection =pika.BlockingConnection(pika.ConnectionParameters(host='192.168.91.85',credentials=credential))
channel =connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)

def on_request(ch,method,props,body):
    number = int(body)
    print('收到的number: ',number)
    print('UUID4: ',props.correlation_id)
    response = fib(number)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body = str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=5) #最大接受量
channel.basic_consume(on_message_callback=on_request,queue='rpc_queue')
channel.start_consuming()