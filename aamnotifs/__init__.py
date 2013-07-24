#!/usr/bin/env python

################################################################################
# Simple notifications implementation with RabbitMQ using pika.
#
# author: Andrei Marcu <andrei@marcu.net>
# https://github.com/andreimarcu/aamnotifs
# Version: 0.1.0
################################################################################

import pika
import time
import json


class Notifs(object):

    def __init__(self, url, exchange="notifs"):
        self.exchange = exchange
        self.connect(url)

    def connect(self, url):
        try:
            self.connection = pika.BlockingConnection(pika.URLParameters(url))
            self.channel = self.connection.channel()
            self.channel.exchange_declare(exchange=self.exchange, type='topic')
        except:
            time.sleep(2)
            self.connect()

    def receive(self, routings, callback):
        if type(routings) == str:
            routings = [routings]

        def internal_callback(ch, method, properties, body):
            body = json.loads(body)
            callback(body["title"], body["message"])

        try:
            result = self.channel.queue_declare(exclusive=True)
            self.queue_name = result.method.queue

            for routing in routings:
                self.channel.queue_bind(exchange=self.exchange,
                                        queue=self.queue_name,
                                        routing_key=routing)
            self.channel.basic_consume(internal_callback, queue=self.queue_name,
                                       no_ack=True)
            self.channel.start_consuming()

        except:
            time.sleep(2)
            self.connect()
            self.receive(routings, callback)

    def send(self, routing, title, message):
        body = json.dumps({"title": title, "message": message})

        try:
            self.channel.basic_publish(exchange=self.exchange,
                                       routing_key=routing, body=body)
        except:
            time.sleep(2)
            self.connect()
            self.channel.basic_publish(exchange=self.exchange,
                                       routing_key=routing, body=body)
