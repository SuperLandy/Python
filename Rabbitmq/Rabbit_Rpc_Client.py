#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import uuid
import time


class FibonacciRpcClient(object):

    def __init__(self):
        '''
        初始化rabbitmq连接
        queue使用随机队列名
        '''
        self.credential = pika.PlainCredentials(
            username='zzq', password='123456')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.91.85',
                                                                            credentials=self.credential))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(
            queue='', exclusive=True)  # 生成一个随机队列名
        self.callback_queue = result.method.queue  # 使用该随机队列名

        self.channel.basic_consume(on_message_callback=self.on_response,
                                   auto_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        '''
        :param ch:
        :param method:
        :param props: rabbit生产者携带的随机值
        :param body: rabbit生产者计算的结果值
        :return:返回rabbit生产者计算值
        '''
        # print('收到的UUID：',props.correlation_id)
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, number):
        '''
        :param number: str  需要计算且斐波那契数列的值
        :return: str  返回斐波那契数列结果值
        '''
        self.response = None
        self.corr_id = str(uuid.uuid4())
        print('发送的UUID：', self.corr_id)
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(number))
        while self.response is None:
            self.connection.process_data_events()  # 如果respnose是空，则做其他事（即非阻塞式）
            print('no message.....')
            time.sleep(1)
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()  # 实例化一个类
response = fibonacci_rpc.call(6)
print('斐波那契值是:', response)
