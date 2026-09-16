def createZMQSocket(self, sock_type):
    sock = self.ZMQcontext.socket(sock_type)
    sock.setsockopt(zmq.LINGER, LINGER_TIME)
    sock.setsockopt(zmq.IPV4ONLY, 0)
    sock.setsockopt(zmq.SNDHWM, 0)
    sock.setsockopt(zmq.RCVHWM, 0)
    try:
        sock.setsockopt(zmq.IMMEDIATE, 1)
    except:
        pass
    if sock_type == zmq.ROUTER:
        sock.setsockopt(zmq.ROUTER_MANDATORY, 1)
    return sock