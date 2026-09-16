def _readline(self):
    if len(self.lines) > 1:
        return self.lines.pop(0)
    tail = ''
    if len(self.lines):
        tail = self.lines.pop()
    try:
        tail += self._read()
    except socket.error:
        logging.exception('No new data')
        time.sleep(0.1)
    self.lines += linesepx.split(tail)
    if len(self.lines) > 1:
        return self.lines.pop(0)