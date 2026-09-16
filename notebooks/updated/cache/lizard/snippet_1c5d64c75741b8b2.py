def poll(self, timeout=None):
    p = select.poll()
    p.register(self._fd, select.POLLIN | select.POLLPRI)
    events = p.poll(int(timeout * 1000))
    if len(events) > 0:
        return True
    return False