def interpret(self, iterable=None, poll_interval=0.2):
    if iterable is None:
        iterable = self.decode(poll_interval)
        if iterable is None:
            return None
    if isinstance(iterable, basestring):
        iterable = self.decode(poll_interval, iterable)
    return interpret_opcodes(iterable)