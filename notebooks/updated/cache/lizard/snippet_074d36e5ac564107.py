def asserts(self, fn, msg_or_fn):
    self.assertions.append((fn, msg_or_fn))
    return self