################################################################################
# Simple(st) example for sending a notification.
################################################################################
import aamnotifs


n = aamnotifs.Notifs("amqps://user:password@domain.tld:5673/%2F")

# The routing_name is the name of the "channel" you want to use
# it can be "mail", "chat", etc.
# This will make it easy to choose which channels your clients
# will receive
n.send("example_channel", "Notification title here", "Notification content here")
