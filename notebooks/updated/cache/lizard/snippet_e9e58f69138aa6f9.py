def maybeReceiveAck(self, ackPacket):
    ackPredicate = self.ackPredicate
    self.ackPredicate = lambda packet: False
    if ackPacket.syn:
        self.synAck()
        return
    if ackPredicate(ackPacket):
        self.ack()