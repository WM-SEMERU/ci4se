def items(self):
    return [(key, value[1]) for key, value in super(LFUCache, self).items()]