#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('user', 'password')

def callback(ch, method, properties, body):
    print (" [x] Received %r" % body.decode())
    time.sleep( body.count(b'.'))
    print (" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='challenge', exchange_type='direct')

channel.queue_declare(queue='test', durable=True)
channel.queue_bind(
        exchange='challenge', queue='test', routing_key='prueba_rmq'
        )
print(' [*] Waiting for messages. To exit press CTRL+C')



channel.basic_consume(queue='test', on_message_callback=callback)

channel.start_consuming()