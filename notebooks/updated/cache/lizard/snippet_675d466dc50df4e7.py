def service(self):
    self.payload, self.payload_peer_address = self.datagram_socket.recvfrom(
        UDP_MAX_DGRAM_LENGTH)
    _logger.debug('Received datagram from peer: %s', self.payload_peer_address)
    if not self.payload:
        self.payload_peer_address = None
        return
    if self.connections.has_key(self.payload_peer_address):
        self.forward()
    else:
        return self.payload_peer_address