def send(self, data):
    if not isinstance(data, C1218Packet):
        data = C1218Packet(data)
    if self.toggle_control:
        if self._toggle_bit:
            data.set_control(ord(data.control) | 32)
            self._toggle_bit = False
        elif not self._toggle_bit:
            if ord(data.control) & 32:
                data.set_control(ord(data.control) ^ 32)
            self._toggle_bit = True
    elif self.toggle_control and not isinstance(data, C1218Packet):
        self.loggerio.warning(
            'toggle bit is on but the data is not a C1218Packet instance')
    data = data.build()
    self.loggerio.debug('sending frame,  length: {0:<3} data: {1}'.format(
        len(data), binascii.b2a_hex(data).decode('utf-8')))
    for pktcount in range(0, 3):
        self.write(data)
        response = self.serial_h.read(1)
        if response == NACK:
            self.loggerio.warning('received a NACK after writing data')
            time.sleep(0.1)
        elif len(response) == 0:
            self.loggerio.error('received empty response after writing data')
            time.sleep(0.1)
        elif response != ACK:
            self.loggerio.error('received unknown response: ' + hex(ord(
                response)) + ' after writing data')
        else:
            return
    self.loggerio.critical('failed 3 times to correctly send a frame')
    raise C1218IOError('failed 3 times to correctly send a frame')