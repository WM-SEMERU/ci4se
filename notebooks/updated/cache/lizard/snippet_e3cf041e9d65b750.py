def receive(self, siz):
    result = bytearray()
    data = 'x'
    while len(data) > 0:
        data = self.sock.recv(siz - len(result))
        result += data
        if len(result) == siz:
            return result
        if len(result) > siz:
            raise Exception('Received more bytes than expected')
    raise Exception('Error receiving data. %d bytes received' % len(result))