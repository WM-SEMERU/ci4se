def close(self):
    yield from self.send('hypervisor close')
    self._writer.close()
    self._reader, self._writer = None