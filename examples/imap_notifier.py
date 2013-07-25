
#!/usr/bin/env python
################################################################################
# imap_notifier.py - IMAP Notifier for aaamnotifs
#
# Andrei Marcu
################################################################################

from imapclient import IMAPClient
from time import sleep
import getpass
import aamnotifs


class Notifier:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
        self.ssl = True
        self.frequency = 3

        self.imap_connection = IMAPClient(self.server, use_uid=True, ssl=self.ssl)
        self.seen_unread = []

        self.imap_connection.login(self.username, self.password)
        self.notifier = aamnotifs.Notifs(
            "amqps://user:password@domain.tld:5673/%2F")

        while True:
            self.check_unread()
            sleep(self.frequency)

    def check_unread(self):
        try:
            self.imap_connection.select_folder("INBOX")
            unread_list = self.imap_connection.search("UNSEEN")
        except:
            self.__init__(self.server, self.username, self.password)
            self.imap_connection.select_folder("INBOX")
            unread_list = self.imap_connection.search("UNSEEN")

        for unread in unread_list:
            if unread not in self.seen_unread:
                self.seen_unread.append(unread)
                envelope = self.imap_connection.fetch(
                    [unread], ["ENVELOPE"])[unread]["ENVELOPE"]
                subject = envelope[1]
                from_name = envelope[2][0][0]

                if not from_name:
                    if envelope[2][0][2] and envelope[2][0][3]:
                        from_name = envelope[2][0][2] + "@" + envelope[2][0][3]
                    else:
                        from_name = "(unknown)"

                if not subject:
                    subject = "(no subject)"

                self.notifier.send("mails", from_name, subject)

if __name__ == '__main__':
    server = raw_input("IMAP server: ")
    username = raw_input("Username: ")
    password = getpass.getpass()
    no = Notifier(server, username, password)

