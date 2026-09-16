def readn(self, n):
    data = ''
    while len(data) < n:
        received = self.sock.recv(n - len(data))
        if not len(received):
            raise socket.error('no data read from socket')
        data += received
    return data