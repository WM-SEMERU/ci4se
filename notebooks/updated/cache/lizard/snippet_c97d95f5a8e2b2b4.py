def popleft(self, block=True, timeout=None):
    return self._pop(block, timeout, left=True)