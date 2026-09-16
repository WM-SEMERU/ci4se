def _send(self, packet):
    fut = self.loop.create_future()
    self.waiters.append((fut, packet))
    if self.waiters and self.in_transaction is False:
        self.protocol.send_packet()
    return fut