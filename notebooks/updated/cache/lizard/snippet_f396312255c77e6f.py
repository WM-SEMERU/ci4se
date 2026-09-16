def Send(self, msg):
    if 'type' not in msg:
        return
    self.sock.send(json.dumps(msg))
    msg = self.sock.recv()
    return msg