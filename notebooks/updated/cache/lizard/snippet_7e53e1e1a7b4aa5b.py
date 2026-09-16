def sendall(self, s):
    while s:
        if self.closed:
            raise socket.error('Socket is closed')
        sent = self.send(s)
        s = s[sent:]
    return None