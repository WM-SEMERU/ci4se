def recv(self, timeout=-1):
    if self.ready:
        return self.other.handover(self)
    return self.pause(timeout=timeout)