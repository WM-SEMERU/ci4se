def handle_raw_packet(self, raw_packet):
    log.debug('got packet: %s', raw_packet)
    packet = None
    try:
        packet = decode_packet(raw_packet)
    except:
        log.exception('failed to parse packet: %s', packet)
    log.debug('decoded packet: %s', packet)
    if packet:
        if 'ok' in packet:
            log.debug('command response: %s', packet)
            self._last_ack = packet
            self._command_ack.set()
        elif self.raw_callback:
            self.raw_callback(raw_packet)
    else:
        log.warning('no valid packet')