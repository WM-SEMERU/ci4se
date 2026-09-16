def __on_message(self, msg):
    msgtype = msg['type']
    msgfrom = msg['from']
    if msgtype == 'groupchat':
        if self._nick == msgfrom.resource:
            return
    elif msgtype not in ('normal', 'chat'):
        return
    self.__callback(msg)