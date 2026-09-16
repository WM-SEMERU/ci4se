def connect(self):
    self.socket = socket.socket()
    self.socket.settimeout(self.timeout_in_seconds)
    try:
        self.socket.connect(self.addr)
    except socket.timeout:
        raise GraphiteSendException(
            'Took over %d second(s) to connect to %s' % (self.
            timeout_in_seconds, self.addr))
    except socket.gaierror:
        raise GraphiteSendException(
            'No address associated with hostname %s:%s' % self.addr)
    except Exception as error:
        raise GraphiteSendException(
            'unknown exception while connecting to %s - %s' % (self.addr,
            error))
    return self.socket