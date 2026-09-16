def close(self):
    self.result_set = None
    if self.impl is not None:
        self.impl._reset()
    self.impl = None