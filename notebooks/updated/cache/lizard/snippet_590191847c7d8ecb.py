def mark_as_read(self, messages, unread=False):
    ids = []
    if isinstance(messages, Inboxable):
        ids.append(messages.fullname)
    elif hasattr(messages, '__iter__'):
        for msg in messages:
            if not isinstance(msg, Inboxable):
                msg = 'Invalid message type: {0}'.format(type(msg))
                raise ClientException(msg)
            ids.append(msg.fullname)
    else:
        msg = 'Invalid message type: {0}'.format(type(messages))
        raise ClientException(msg)
    retval = self.reddit_session._mark_as_read(ids, unread=unread)
    return retval