def get(self, timeout=None, block=True):
    return self.get_event(timeout, block).data