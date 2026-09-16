def group_write(self, addr, data, dptsize=0):
    cemi = CEMIMessage()
    cemi.init_group_write(addr, data, dptsize)
    with self._lock:
        self.send_tunnelling_request(cemi)
        if self._write_delay:
            time.sleep(self._write_delay)