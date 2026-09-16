def process_data(self, new_data):
    self.buffer.feed(new_data)
    for line in self.buffer:
        log.debug('FROM SERVER: %s', line)
        if not line:
            continue
        self._process_line(line)