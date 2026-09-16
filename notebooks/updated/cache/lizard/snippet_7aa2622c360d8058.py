def msg(self, msg=None, ret_r=False):
    if msg or ret_r:
        self._msg = msg
        return self
    return self._msg