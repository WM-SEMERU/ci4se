def popleft(self):
    self._mq.send('^', True, type=1)
    message = self._wait_receive_msg()
    reply = int(message[0].decode('utf-8'))
    if reply == -1:
        raise IndexError('pop from empty list')
    return reply