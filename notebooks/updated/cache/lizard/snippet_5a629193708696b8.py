def sendOACK(self):
    log.debug('In sendOACK with options %s', self.context.options)
    pkt = TftpPacketOACK()
    pkt.options = self.context.options
    self.context.sock.sendto(pkt.encode().buffer, (self.context.host, self.
        context.tidport))
    self.context.last_pkt = pkt