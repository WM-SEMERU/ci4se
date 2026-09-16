def message(self, username, message_text):
    if not isinstance(username, six.string_types):
        username = username.username
    for mailbox in (self.inbox, self.outbox):
        for thread in mailbox:
            if thread.correspondent.lower() == username.lower():
                thread.reply(message_text)
                return
    return self._message_sender.send(username, message_text)