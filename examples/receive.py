################################################################################
# Simple(st) example for receiving notifications.
################################################################################
import aamnotifs


def print_all_notifications(title, message):
    print "Notification received: {0}: {1}".format(title, message)


def print_mail_and_irc_notifications(title, message):
    print "Mail and IRC notifications received: {0}: {1}".format(title, message)

try:
    n = aamnotifs.Notifs("amqps://user:password@domain.tld:5673/%2F")

    # The routing_name is the name of the "channel" you want to use
    # it can be "mail", "chat", etc.
    # This will make it easy to choose which channels your clients
    # will receive. Can be a list too, for listening on multiple streams.
    n.receive("#", print_all_notifications)  # "#" matches all channels

    # OR n.receive(["mail", "irc"], print_mail_and_irc_notifications)

except KeyboardInterrupt:
    break
