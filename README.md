aamnotifs
=========

Simple notifications implementation with RabbitMQ using pika.

Requirements
------------
* Python 2.6+
* pika


Usage
-----
Best illustrated in the provided examples but this is the basic idea: 

Connect to the RabbitMQ server:
```python
n = notifs.Notifs("amqps://user:password@domain.tld:5673/%2F")
```

Send a message:
```python
n.send("test_channel", "Notification title", "Notification content")
```

Listen for messages:
```python
n.receive("test_channel", callback_function)
```

Author
-------
Andrei Marcu  
http://andreim.net/