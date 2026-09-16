def receive(self, message_type):
    topic = None
    message = None
    if message_type == RAW:
        message = self._sock.recv(flags=zmq.NOBLOCK)
    elif message_type == PYOBJ:
        message = self._sock.recv_pyobj(flags=zmq.NOBLOCK)
    elif message_type == JSON:
        message = self._sock.recv_json(flags=zmq.NOBLOCK)
    elif message_type == MULTIPART:
        data = self._sock.recv_multipart(flags=zmq.NOBLOCK)
        message = data[1]
        topic = data[0]
    elif message_type == STRING:
        message = self._sock.recv_string(flags=zmq.NOBLOCK)
    elif message_type == UNICODE:
        message = self._sock.recv_unicode(flags=zmq.NOBLOCK)
    else:
        raise Exception('Unknown message type %s' % (self._message_type,))
    return topic, message