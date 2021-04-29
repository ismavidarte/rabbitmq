#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('user', 'password')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='challenge', exchange_type='direct')

channel.queue_declare(queue='test', durable=True)
channel.queue_bind(
        exchange='challenge', queue='test', routing_key='prueba_rmq'
        )

while 1>0:

    message = "Message sent to worker"
    channel.basic_publish(exchange='challenge',
                          routing_key='prueba_rmq',
                          body=message,
                          properties=pika.BasicProperties(
                             delivery_mode = 2,
                          ))
    print(" [x] Sent %r" % message)
connection.close()