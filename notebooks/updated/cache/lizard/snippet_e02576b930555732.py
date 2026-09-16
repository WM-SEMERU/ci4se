def sub(self, topics=(b'',)):
    sock = self.__sock(zmq.SUB)
    for topic in topics:
        if not isinstance(topic, bytes):
            error = 'Topics must be a list of bytes'
            log.error(error)
            raise TypeError(error)
        sock.setsockopt(zmq.SUBSCRIBE, topic)
    return self.__recv_generator(sock)