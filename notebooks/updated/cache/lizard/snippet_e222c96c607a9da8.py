def set_org(self, value, lineno):
    if value < 0 or value > MAX_MEM:
        error(lineno, 
            'Memory ORG out of range [0 .. 65535]. Current value: %i' % value)
    self.index = self.ORG = value