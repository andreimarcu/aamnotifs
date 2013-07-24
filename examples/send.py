################################################################################
# Simple(st) example for sending a notification.
################################################################################
import notifs


n = notifs.Notifs("amqps://user:password@domain.tld:5673/%2F")

# The routing_name is the name of the "channel" you want to use
# it can be "mail", "chat", etc.
# This will make it easy to choose which channels your clients
# will receive
n.send("test_channel", "Title here", "Content here")
