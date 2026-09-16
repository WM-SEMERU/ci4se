def next(self):
    if not self.keep_packets:
        return self._packet_generator.send(None)
    elif self._current_packet >= len(self._packets):
        packet = self._packet_generator.send(None)
        self._packets += [packet]
    return super(FileCapture, self).next_packet()