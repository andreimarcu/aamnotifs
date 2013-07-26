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
n.send("test_channel_one", "Notification title", "Notification content")
n.send("test_channel_two", "Notification title", "Notification content")
```

Listen for messages:
```python
n.receive("test_channel_one", callback_function)

# OR n.receive(["test_channel_one", "test_channel_two"], callback_function)
# or even n.receive(["#"], callback_function)  # wildcard matches all channels

```

Author
-------
Andrei Marcu  
http://andreim.net/