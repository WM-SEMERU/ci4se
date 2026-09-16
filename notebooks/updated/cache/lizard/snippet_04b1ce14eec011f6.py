def _bind(self):
    if not zmq:
        return
    self.context = zmq.Context()
    self.socket = self.context.socket(zmq.PUB)
    self.socket.bind('tcp://*:%i' % self.port)