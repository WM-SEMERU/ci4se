def connectionJustEstablished(self):
    assert not self.disconnecting
    assert not self.disconnected
    try:
        p = self.factory.buildProtocol(PTCPAddress(self.peerAddressTuple,
            self.pseudoPortPair))
        p.makeConnection(self)
    except:
        log.msg('Exception during PTCP connection setup.')
        log.err()
        self.loseConnection()
    else:
        self.protocol = p