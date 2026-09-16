def _handle_watch_message(self, message):
    if self.log_protocol_level is not None:
        logger.log(self.log_protocol_level, '<- %s', hexlify(message).decode())
    message = self.pending_bytes + message
    while len(message) >= 4:
        try:
            packet, length = PebblePacket.parse_message(message)
        except IncompleteMessage:
            self.pending_bytes = message
            break
        except:
            expected_length, = struct.unpack('!H', message[:2])
            if expected_length == 0:
                self.pending_bytes = b''
            else:
                self.pending_bytes = message[expected_length + 4:]
            raise
        self.event_handler.broadcast_event('raw_inbound', message[:length])
        if self.log_packet_level is not None:
            logger.log(self.log_packet_level, '<- %s', packet)
        message = message[length:]
        self.event_handler.broadcast_event((_EventType.Watch, type(packet)),
            packet)
        if length == 0:
            break
    self.pending_bytes = message