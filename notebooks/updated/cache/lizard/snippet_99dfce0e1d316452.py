def sendConnect(self, data):
    if self.backend == 'ZMQ':
        import zmq
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.DEALER)
        self.socket.setsockopt(zmq.IDENTITY, b'launcher')
        self.socket.connect('tcp://127.0.0.1:{port}'.format(port=self.
            brokerPort))
        self.socket.send_multipart([b'CONNECT', pickle.dumps(data, pickle.
            HIGHEST_PROTOCOL)])
    else:
        pass