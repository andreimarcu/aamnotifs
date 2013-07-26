################################################################################
# Simple(st) example for receiving notifications.
################################################################################
import notifs


def print_notification(title, message):
    print "Print notification received: {0}: {1}".format(title, message)

def web_app_notify(title, message):
    print "Webapp notification received: {0}: {1}".format(title, message)
 
def iphone_app_notify(title, message):
    print "iPhone App notification received: {0}: {1}".format(title, message)
 
def android_app_notify(title, message):
    print "Android App notification received: {0}: {1}".format(title, message)

try:
    n = notifs.Notifs("amqps://user:password@domain.tld:5673/%2F")

    # The routing_name is the name of the "channel" you want to use
    # it can be "mail", "chat", etc.
    # This will make it easy to choose which channels your clients
    # will receive. Can be a list too, for listening on multiple streams.
    n.receive("test_channel", print_notification)
    n.receive("test_channel", web_app_notify)
    n.receive("test_channel", iphone_app_notify)
    n.receive("test_channel", android_app_notifify)

except KeyboardInterrupt:
    break
