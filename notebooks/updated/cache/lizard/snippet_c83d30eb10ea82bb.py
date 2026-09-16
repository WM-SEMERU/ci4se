def handle_version(self, message_header, message):
    log.debug('handle version')
    verack = VerAck()
    log.debug('send VerAck')
    self.send_message(verack)
    self.verack = True
    self.send_getheaders(self.first_block_hash)