def subscribe(self, topic=b''):
    self.sockets[zmq.SUB].setsockopt(zmq.SUBSCRIBE, topic)
    poller = self.pollers[zmq.SUB]
    return poller