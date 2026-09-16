def new(self, val):
    if len(self.things) >= self.max_things:
        raise LimitationError('too many things')
    self.things.add(val)
    return val